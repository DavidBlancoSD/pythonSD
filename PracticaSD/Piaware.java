/**
@author Francisco Manuel Morales Carlin
@author David Blanco Cañizares
*/

package eventos; 

public class Piaware {

	private String rpi;
	private float latitud;
	private float longitud;
	private float cpuinuse;
	private float memavailable;
	private float cputempav;
	private float cputemperature;
	private float casetemperature;
	private float casetempav;
	private float ambienttemp;
	private float ambienttempav;
	private String timeRegister;

	public Piaware(String rpi, float lat, float lon, float cpuinuse, float memavailable, float cputempav,
					float cputemperature, float casetemperature, float casetempav,float ambienttemp, float ambienttempav, String tr){

			this.rpi = rpi;
			this.latitud = lat;
			this.longitud = lon;
			this.cpuinuse = cpuinuse;
			this.memavailable = memavailable;
			this.cputempav = cputempav;
			this.cputemperature = cputemperature;
			this.casetemperature = casetemperature;
			this.casetempav = casetempav;
			this.ambienttemp = ambienttemp;
			this.ambienttempav = ambienttempav;
			this.timeRegister = tr;

	}
	public Piaware(){}

	public String getrpi(){ return this.rpi;}
	public float getlatitude(){return this.latitud;}
	public float getlongitud(){return this.longitud;}
	public float getCpuinuse(){return this.cpuinuse;}
	public float getMemavailable(){return this.memavailable;}
	public float getCputempav(){return this.cputempav;}
	public float getCputemperature(){return this.cputemperature;}
	public float getCasetemperature(){return this.casetemperature;}
	public float getCasetempav(){return this.casetempav;}
	public float getAmbienttemp(){return this.ambienttemp;}
	public float getAmbienttempav(){return this.ambienttempav;}
	public String getTimeRegister(){return this.timeRegister;}

	public void setrpi(String rpi){this.rpi = rpi;}
	public void setlatitude(float la){this.latitud = la;}
	public void setlongitud(float lon){this.longitud = lon;}
	public void setCpuinuse(float cpuinuse){this.cpuinuse = cpuinuse;}
	public void setMem(float mem){this.memavailable = mem;}
	public void setCputempav(float cputempav){this.cputempav = cputempav;}
	public void setCputemp(float cputemp){this.cputemperature = cputemp;}
	public void setCasetemp(float casetemp){this.casetemperature = casetemp; }
	public void setCasetempav(float casetempav){this.casetempav = casetempav;}
	public void setAmbienttemp(float amtemp){this.ambienttemp = amtemp;}
	public void setAmbienttempAV(float amtempav){this.ambienttempav = amtempav;}
	public void setTimeRegister(String timer){this.timeRegister = timer;}
	
	@Override
	public String toString() {
		return "Piaware [rpi=" + this.rpi + ", latitud=" + this.latitud 
				+ ", longitud=" + this.longitud + ", time=" + this.timeRegister
				+ ", cpu en uso" + this.cpuinuse + ", memoria disponible" + this.memavailable
				+ ", temperaturaCPU" + this.cputemperature + ", temperatura media" + this.cputempav
				+ ", temperatura carcasa" + this.casetemperature + ", temperaturaCarcasaMedia" + this.casetempav
				+ ", temperatura ambiente" + this.ambienttemp + ", temperatura ambiente media" + this.ambienttempav
				+ "]";
	}
}