import tkinter as tk
import numpy as np
from sqlite3 import *
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    

class Skin:
    
    """This class helps you to calculate all sorts of skin phenomenon and analize it.
    Hereafter skin refers back to any reason reduces the oil well production and causes pressure drop
    in that well."""
    
    """
        Rw (inches):    Well radius
    """
    
    all_skins = ['perforation', 'gravel', 'slanted well', 'partial', 'non Darcy', 'result']
    
    def __init__(self, Rw):
    
        self.Rw = float(Rw)
    
    def perforation(self, lp, theta, spf, Rd, Rc, Rp, anisotropy, damage_ratio, crushed_ratio):
        
        """This function helps you to find skin due to the perforation job.
            We know that the total perforation skin is the sum of vertical, horizontal,
            wellbore and crushed zone skin. In other word:
            Sp = Swb + Sc + Sh + Sv
            
            lp (inches):    perforation Length
            theta:  Phasing angle in degree
            SPF: shut density
            Kv/Kh:  anisotropy
            Kd/K:   damage permeability to res. permeability
            Kc/k:  crushed permeability to res. permeability
            Rd (inches):  damage zone radius
            Rc (inches):  crushed zone radius
            Rp (inches):  Perforation tunnel radius
            h (inches): spaced between perforations
        """
        
        lp = float(lp)
        theta = int(theta); spf = int(spf); Rd = float(Rd); Rc = float(Rc); Rp = float(Rp); anisotropy = float(anisotropy); damage_ratio = float(damage_ratio); crushed_ratio = float(crushed_ratio)
        
                    
        
        ld = Rd - self.Rw
        h = 12 / spf
        RpD = (Rp / (2*h)) * (1 + (anisotropy ** 0.5))
        hD = (h / lp) * ((1 / anisotropy) ** 0.5)
        RwD = (self.Rw / (self.Rw + lp))
        
        #connecting to our database
        conn = connect(resource_path('tables.db'))
        c = conn.cursor()
        
        a1 = c.execute(f"""SELECT a1 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        a2 = c.execute(f"""SELECT a2 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        b1 = c.execute(f"""SELECT b1 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        b2 = c.execute(f"""SELECT b2 FROM perforation_vertical where phasing == {theta} LIMIT 500""").fetchone()[0]
        C1 = c.execute(f"""SELECT C1 FROM perforation_wellbore where phasing == {theta} LIMIT 500""").fetchone()[0]
        C2 = c.execute(f"""SELECT C2 FROM perforation_wellbore where phasing == {theta} LIMIT 500""").fetchone()[0]
        a = a1 * np.log10(RpD) + a2
        b = b1 * RpD + b2
        
        if ld > lp:
            if theta == 0:
                
                Sh = np.log((4*self.Rw) / lp)
                
            
            else:
                
                Sh = np.log((self.Rw) / (c.execute(f"""SELECT alpha FROM [perforation_horizontal] WHERE phasing == {theta} LIMIT 500""") * (self.Rw + lp)))
                
            Sv = (10 ** a) * (hD ** (b - 1)) * (RpD ** b)
            Swb = C1 * np.exp(C2 * RwD)
            Sc = (h / lp) * ((1 / crushed_ratio) - 1) * np.log(Rc / Rp)
            Sp = Sv + Swb + Sc + Sh
            Sp = ((1 / damage_ratio) - 1) * np.log(Rd/self.Rw) + (1 / damage_ratio) * Sp
            
        elif ld < lp:
            
            lp_prime = lp - (1 - damage_ratio) * ld
            Rw_prime = self.Rw + (1 - damage_ratio) * ld 
            hD_prime = (h / lp_prime) * ((1 / anisotropy) ** 0.5)
            RwD_prime = (Rw_prime) / (Rw_prime + lp_prime)
            
            if theta == 0:
                
                Sh = np.log((4*self.Rw) / lp_prime)
                            
            else:
                
                Sh = np.log((self.Rw) / (c.execute(f"""SELECT alpha FROM [perforation_horizontal] WHERE phasing == {theta} LIMIT 500""").fetchone()[0] * (Rw_prime + lp_prime)))
            
            Sv = (10 ** a) * (hD_prime ** (b - 1)) * (RpD ** b)
            Swb = C1 * np.exp(C2 * RwD_prime)
            Sc = (h / lp_prime) * ((1 / crushed_ratio) - 1) * np.log(Rc / Rp)
            Sp = Sv + Swb + Sc + Sh
        
        conn.commit()
        conn.close()
        
        Sp=float("%0.4f" % Sp)
        
        return Sp
        
        
    def golan(self, lp, k, h, spf, mesh_size):
        
        """This function helps you to find skin due to the Gravel pack job.
            Sg=96*(K*h*Lp)/(Kg*Dper^2*n)
            ----------------------------
            Dgg=(2.45*10^-10*γg*k*h*Lp*βg) / (µ*Dper^4*n^2)
            ----------------------------
            Dgo=(1.8*10^-11*Bo*ρ*k*h*Lp*βg) / (µ*Dper^4*n^2)
            ----------------------------
            βg=b*Kg^(-a)
            
            Sg:    gravel skin
            K (mD):  Permeability
            h (ft): reservoir thickness
            Lp (in): gravel packed perforation length
            Kg (mD):    permeability of gravel
            Dperf = perforation diameter (in)
            γg = gas gravity
            µ (cp)= fluid viscosity 
            ρ (lbm/ft3)= fluid density
            n = number of perforations
            βg= gravel turbulence factor
            well type = gas well or oil well
        """
        
        lp=float(lp); k=float(k); h=float(h); spf=int(spf)
        
        #connecting to our database
        conn = connect(resource_path('tables.db'))
        c = conn.cursor()
        mesh_size=f"'{mesh_size}'"
        a=c.execute(f"""SELECT a FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        b=c.execute(f"""SELECT b FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        kg=c.execute(f"""SELECT permeability FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        Bg=b*(kg**(-a))
        dperf=c.execute(f"""SELECT mean_diameter FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        n=h*spf
        
        conn.close()
        
        # if well_type=='gas well':
            # D=(2.45*(10**(-10))*gas_gravity*k*h*lp*Bg) / (miu*(dperf**4)*(n**2))
        # elif well_type=='oil well':
            # D=(1.8*(10**(-11))*oil_FVF*rou*k*h*lp*Bg) / (miu*(dperf**4)*(n**2))
            
        Sg=96*(k*h*lp)/(kg*(dperf**2)*n)
        
        Sg=float("%0.4f" % Sg)
        
        return Sg
    
    def furui(self, lp, rp, tc, spf, theta, k, rw, mesh_size):
        
        """This function helps you to find skin due to Gravel pack installation using Furui (2004) method.
                Lp (in): gravel packed perforation length
                theta (degrees): phasing angel
                rp (in.): perforation radius
                rw (in.): well radius
                tc (in.): Casing thickness
                spf: shut density per foot
                k (mD): Reservoir permeability
            """
            
        lp=float(lp); rp=float(rp); tc=float(tc); theta=float(theta); k=float(k); rw=float(rw); spf=int(spf)
        
        #connecting to our database
        conn = connect(resource_path('tables.db'))
        c = conn.cursor()
        mesh_size=f"'{mesh_size}'"
        kcg=c.execute(f"""SELECT permeability FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        rpD=rp/rw
        hp=12/spf
        hpD=hp/rw
        tcD=tc/rw
        kcgD=kcg/k
        BcgD=1/kcgD
        Scgic0=((2*hpD*tcD)/(kcgD*(rpD**2)))
        Ftcgic=(((2*hpD)/(rpD**2))**2)*BcgD*tcD
        sp0=-0.163
        v=np.sin(np.deg2rad(theta))
        spl0=(3*hpD)/(2*rpD)+np.log((v**2)/((hpD**2)*(1+v)))-0.61
        heD=hp/lp
        reD=rp/hp
        lpD=lp/rw
        Ftp=1+((heD)/(lpD))*(1/(reD)-2)
        Ftpl=(((hpD)/(rpD))**2)*((27)/(24*rpD))+((16)/(3*hpD))-((3*v+4)/(v*(v+1)))
        Scgoc0=(1-((kcgD)**(-0.5)))*sp0+((kcgD)**(-0.5))*spl0
        Ftcgoc=(1-((kcgD)**(-0.5)))*Ftp+(((kcgD)**(-0.5)))*(Ftpl)
        Scg0=Scgic0+Scgoc0
        Ftcg=Ftcgic+Ftcgoc
        kg=c.execute(f"""SELECT permeability FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        
        # close the database
        conn.close()
        
        Scg0=float("%0.4f" % Scg0)
        
        return Scg0

    def muskat_top(self, h, hw, rw, re):
        
        """This function helps you to find skin due to partial penetration using muskat (1946) method.
            this method is used for circumstances when the completion is in the top of the pay zone.                                   
                h (ft): reservoir thickness
                hw (ft): completion thickness thickness
                rw (ft): well radius
                re (ft): Drainage area radius
            """
        
        h=float(h); hw=float(hw); rw=float(rw); re=float(re)
        
        Spc = ((h/hw)/(1+7*(((rw)/(2*hw))**0.5)*np.cos((np.pi*hw)/(2*h)))-1)*np.log(re/rw)

        Spc=float("%0.4f" % Spc)
        
        return Spc

    def muskat_middle(self, h, hw, rw, re):
    
        """This function helps you to find skin due to partial penetration using muskat (1946) method.
            this method is used for circumstances when the completion is in the center of the pay zone.                                   
                h (ft): reservoir thickness
                hw (ft): completion thickness thickness
                rw (ft): well radius
                re (ft): Drainage area radius
            """
        
        h=float(h); hw=float(hw); rw=float(rw); re=float(re)
        
        Spc = ((h/hw)/(1+7*(((rw)/(hw))**0.5)*np.cos((np.pi*hw)/(2*h)))-1)*np.log(re/rw)

        Spc=float("%0.4f" % Spc)

        return Spc
        
    def odeh(self, h, hw, rw, I, zm):

        """This function helps you to find skin due to partial penetration using Odeh (1980) method.                                 
                h (ft): reservoir thickness
                hw (ft): completion thickness thickness
                rw (ft): well radius
                I: anisotropy or Kv/Kh
                zm (ft): the distance of middle of the completion to the top of the pay zone.
            """
            
        h=float(h); hw=float(hw); rw=float(rw); I=float(I); zm=float(zm)
            
        rwc=rw*np.exp(0.2126*(zm/h+2.753))
        Spc = 1.35*(((h/hw)-1)**0.835)*(np.log(h/I+7)-1.95-(np.log(rwc)*(0.49+0.1*np.log(h/I))))

        Spc=float("%0.4f" % Spc)
        
        Spc=float("%0.4f" % Spc)
        
        return Spc
        
    def papatzacos(self, h, hw, rw, I, h1):
        
        """This function helps you to find skin due to partial penetration using Papatzacos (1987) method.                                 
                h (ft): reservoir thickness
                hw (ft): completion thickness thickness
                rw (ft): well radius
                I: anisotropy or Kv/Kh
                h1 (ft): the distance of top of the completion to the top of the pay zone.
            """
        
        h=float(h); hw=float(hw); rw=float(rw); I=1/float(I); h1=float(h1);
            
        hwD=hw/h
        rD=(rw/h)*I
        h1D=h1/h
        A=1/(h1D+hwD/4)
        B=1/(h1D+3*hwD/4)
        Spc = ((1/hwD)-1)*np.log(np.pi/(2*rD))+(1/hwD)*np.log((hwD/(2+hwD))*(((A-1)/(B-1))**0.5))
        
        Spc=float("%0.4f" % Spc)
        
        return Spc
            
    def cinco(self, h, rw, I, theta):
    
        """This function helps you to find skin due to deviation of the well using Cinco et al. (1975) method.                                 
            h (ft): reservoir thickness
            theta : deviation angel from vertical
            rw (ft): well radius
            I: anisotropy or Kv/Kh
        """
        h=float(h); rw=float(rw); I=float(I); theta=float(theta)
        
        theta_prime=np.arctan(I*np.tan(np.deg2rad(theta)))
        
        S_theta=-((theta_prime/41)**2.06)-(((theta_prime/56)**1.865)*np.log10(h/(100*I*rw)))
        
        Spc=float("%0.4f" % Spc)
        
        return S_theta
        
        
    def besson(self, h, rw, I, theta):
    
        """This function helps you to find skin due to deviation of the well using Besson (1990) method.                                 
            h (ft): reservoir thickness
            theta : deviation angel from vertical
            rw (ft): well radius
            I: anisotropy or Kv/Kh
        """
    
        h=float(h); rw=float(rw); I=float(I); theta=float(theta)
        
        gamma=((1/(I**2))+(1-(1/(I**2)))*(np.cos(np.deg2rad(theta))**2))**0.5
        
        S_theta=np.log((4*rw*np.cos(np.deg2rad(theta)))/(h*I*gamma))+(np.cos(np.deg2rad(theta))/gamma)*np.log(((2*I*(gamma**0.5))/(1+1/gamma))*((h)/(4*rw*(np.cos(np.deg2rad(theta))**0.5))))
        
        S_theta=float("%0.4f" % S_theta)
        
        return S_theta
        
        
    def non_darcy_gas_cased(self, h, hw, gamma, k, lp, miu, spf, mesh_size, q):
        
        """This function helps you to find skin due to nondarcy flow of an gravel installed gas well..
            Sg=96*(K*h*Lp)/(Kg*Dper^2*n)
            ----------------------------
            Dgg=(2.45*10^-10*γg*k*h*Lp*βg) / (µ*Dper^4*n^2)
            ----------------------------
            βg=b*Kg^(-a)
            
            Sg:    gravel skin
            K (mD):  Permeability
            h (ft): reservoir thickness
            Lp (in): gravel packed perforation length
            Kg (mD):    permeability of gravel
            Dperf = perforation diameter (in)
            γg = gas gravity
            µ (cp)= fluid viscosity 
            ρ (lbm/ft3)= fluid density
            n = number of perforations
            βg= gravel turbulence factor
        """
        
        h=float(h); hw=float(hw); gamma=float(gamma); k=float(k); lp=float(lp); miu=float(miu); spf=float(spf); mesh_size; q=float(q)
        
        #connecting to our database
        conn = connect(resource_path('tables.db'))
        c = conn.cursor()
        mesh_size=f"'{mesh_size}'"
        a=c.execute(f"""SELECT a FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        b=c.execute(f"""SELECT b FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        kg=c.execute(f"""SELECT permeability FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        Bg=b*(kg**(-a))
        dperf=c.execute(f"""SELECT mean_diameter FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        n=hw*spf
        
        Dgg=(2.45*(10**(-10))*gamma*k*h*lp*Bg) / (miu*(dperf**4)*n**2)
        
        Sn=Dgg*q
      
        Sn=float("%0.4f" % Sn)
        
        return Sn
        
    def non_darcy_oil_cased(self, h, hw, Bo, density, k, lp, miu, spf, mesh_size, q):
    
        """This function helps you to find skin due to nondarcy flow of an gravel installed oil well..
            Sg=96*(K*h*Lp)/(Kg*Dper^2*n)
            ----------------------------
            Dgo=(1.8*10^-11*Bo*ρ*k*h*Lp*βg) / (µ*Dper^4*n^2)
            ----------------------------
            βg=b*Kg^(-a)
            
            Sg:    gravel skin
            K (mD):  Permeability
            h (ft): reservoir thickness
            Lp (in): gravel packed perforation length
            Kg (mD):    permeability of gravel
            Dperf = perforation diameter (in)
            µ (cp)= fluid viscosity 
            ρ (lbm/ft3)= fluid density
            n = number of perforations
            Bo = Oil FVF (BBL/STB)
            βg= gravel turbulence factor
        """
        
        h=float(h); hw=float(hw); density=float(density); k=float(k); lp=float(lp); miu=float(miu); spf=float(spf); mesh_size; q=float(q); Bo=float(Bo)
        
        #connecting to our database
        conn = connect(resource_path('tables.db'))
        c = conn.cursor()
        mesh_size=f"'{mesh_size}'"
        a=c.execute(f"""SELECT a FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        b=c.execute(f"""SELECT b FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        kg=c.execute(f"""SELECT permeability FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        Bg=b*(kg**(-a))
        dperf=c.execute(f"""SELECT mean_diameter FROM [Gravel_Properties] where mesh_size == {mesh_size} LIMIT 500""").fetchone()[0]
        n=hw*spf
        
        Dgo=(1.8*(10**(-11))*Bo*density*k*h*lp*Bg) / (miu*(dperf**4)*n**2)
        
        Sn=Dgo*q

        Sn=float("%0.4f" % Sn)
        
        return Sn
        
    def non_darcy_open(self, h, hw, gamma, k, rw, miu, q):
    
        """This function helps you to find skin due to nondarcy flow of an open-hole well.                                 
            rw (ft): well radius
            gamma = gas gravity
            K (mD):  Permeability
            h (ft): reservoir thickness
            hw (ft): completion thickness
            miu (cp): fluid viscosity
            q (MscfD): 
        """
        h=float(h); hw=float(hw); gamma=float(gamma); k=float(k); rw=float(rw); miu=float(miu); q=float(q)
        
        B=2.33*(10**10)*(k**(-1.2))
        D=2.22*(10**(-15))*(B*gamma*k*h)/((hw**2)*rw*miu)
        
        Sn=D*q
        
        Sn=float("%0.4f" % Sn)
        
        return Sn
        
        