/**
@author Francisco Manuel Morales Carlin
@author David Blanco Cañizares
*/

package eventos;

import org.mule.api.annotations.ContainsTransformerMethods;
import org.mule.api.annotations.Transformer;
import org.mule.module.json.JsonData;

import eventos.Piaware;

@ContainsTransformerMethods
public class TransformerforPi
{
	@Transformer
	public Piaware JsonDataToPiaware(JsonData obj) throws Exception
	{
		Piaware evento = new Piaware();

		evento.setrpi(obj.getAsString("channel/name"));
		evento.setabouts(obj.getAsString("channel/description"));
		evento.setlatitude(Float.parseFloat(obj.getAsString("channel/description")));
		evento.setlongitud(Float.parseFloat(obj.getAsString("channel/description")));
		evento.setTimeRegister(obj.getAsString("channe/updated_at"));

		evento.setCpuinuse(Float.parseFloat(obj.getAsString("feeds[1]/field1")));
		evento.setMem(Float.parseFloat(obj.getAsString("feeds[1]/field2")));
		evento.setCputempav(Float.parseFloat(obj.getAsString("feeds[1]/field3")));
		evento.setCputemp(Float.parseFloat(obj.getAsString("feeds[1]/field4")));
		evento.setCasetemp(Float.parseFloat(obj.getAsString("feeds[1]/field5")));	
		evento.setCasetempav(Float.parseFloat(obj.getAsString("feeds[1]/field6")));
		evento.setAmbienttemp(Float.parseFloat(obj.getAsString("feeds[1]/field7")));
		evento.setAmbienttempAV(Float.parseFloat(obj.getAsString("feeds[1]/field8")));
		
		return evento;
	}
}