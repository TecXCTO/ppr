import math

class PrimitiveParameters():
  def __init__( self, *args, **kwargs ):
    light_speed: "299792458", # In Vaccum Meter per Second.
    phi: "3.141592653589793"
    self.electricity_parameters = {
      max_frequency_of_electricity : "",
      max_volt : "",
      max_current : "",
      max_practical_frequency_of_electricity : "",
      max_practical_volt : "",
      max_practical_current : "",
      min_frequency_of_electricity  : "",
      min_volt   : "",
      min_current   : "",
      min_practical_frequency_of_electricity   : "",
      min_practical_volt  : "" ,
      min_practical_current : "",
      max_electric_field : "",
      min_electric_field : "",
      max_electric_field_frequency : "",
      min_electric_field_frequency : "",
      max_electric_field_wavelength : "",
      min_electric_field_wavelength : "",
      max_electric_field_speed : "1/math.sqrt(vaccum_permittivity*vaccum_permeability)", # Permittivity is critical in determining the speed of electromagnetic waves
      min_electric_field_speed : "1/math.sqrt(material_permittivity*material_permeability)",
      vaccum_permittivity : "8.854*10e-12", # unit in F/M Farad per meter of SI
      reletive_permittivity : "",
      material_permittivity : "",
    
    }  
    
    self.magnetism_parameters = {
      max_magnetic_field : "",
      min_magnetic_field : "",
      max_magnetic_field_frequency : "",
      min_magnetic_field_frequency : "",
      max_magnetic_field__wavelength : "",
      min_magnetic_field__wavelength : "",
      max_magnetic_field_speed : "1/math.sqrt(vaccum_permittivity*vaccum_permeability)",
      min_magnetic_field_speed : "1/math.sqrt(material_permittivity*material_permeability)",
      vaccum_permeability : "4*phi*10e-7",
      reletive_permeability: "",
      material_permeability: "",
      light_speed: "299792458", # In Vaccum Meter per Second.
      phi: "3.141592653589793"
    }
    self.electricity_corresponding_parameters = {
      max_frequency : "",
      max_volt_corresponding_to_max_frequency: "",
      max_current_corresponding_to_max_frequency : "",
      min_volt_corresponding_to_max_frequency: "",
      min_current_corresponding_to_max_frequency : "",
      max_practical_frequency : "",
      max_volt_corresponding_to_max_practical_frequency: "",
      max_current_corresponding_to_max_practical_frequency : "",
      max_practical_volt_corresponding_to_max_practical_frequency: "",
      max_practical_current_corresponding_to_max_practical_frequency : "",
      min_practical_volt_corresponding_to_max_practical_frequency: "",
      min_practical_current_corresponding_to_max_practical_frequency : "",
      min_volt_corresponding_to_max_practical_frequency: "",
      min_current_corresponding_to_max_practical_frequency : "",
      
      max_practical_volt : "",
      
      max_practical_current : "",
      
      min_frequency  : "",
      
      
      min_volt   : "",
      
      min_current   : "",
      
      min_practical_frequency   : "",
      
      min_practical_volt  : "" ,
      
      min_practical_current : "",
    }

  def primitive_radius():
  
  parameters = {
    
  max_frequency : "",
  max_volt : "",
  max_current : "",
  max_practical_frequency : "",
  max_practical_volt : "",
  max_practical_current : "",
  min_frequency  : "",
  min_volt   : "",
  min_current   : "",
  min_practical_frequency   : "",
  min_practical_volt  : "" ,
  min_practical_current : "",
  
  }
