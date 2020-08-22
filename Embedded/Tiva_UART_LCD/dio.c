#include "dio.h"

void DIO_FlipPort(uint8_t port_index, uint8_t pins_mask){
	switch(port_index) {
		case 0 :// PORTA selected
			GPIO_PORTA_DATA_R ^= pins_mask;
		break;
		case 1 :// PORTA selected
			GPIO_PORTB_DATA_R ^= pins_mask;
		break;
		case 2 :// PORTA selected
			GPIO_PORTC_DATA_R ^= pins_mask;
		break;
		case 3 :// PORTA selected
			GPIO_PORTD_DATA_R ^= pins_mask;
		break;
		case 4:
			GPIO_PORTE_DATA_R ^= pins_mask;
		break;
		case 5:
			GPIO_PORTF_DATA_R ^= pins_mask;
		break;
		}
}
void DIO_WritePort(uint8_t port_index, uint8_t pins_mask,Dio_LevelType pins_level)
{
	 

	switch(port_index){
		case 0 : // if port A
			if(pins_level == STD_LOW)
		 GPIO_PORTA_DATA_R&=~(pins_mask);
			else
				GPIO_PORTA_DATA_R|=pins_mask;
		break;
		
		
		case 1: // if port B
		if(pins_level == STD_LOW)
		 GPIO_PORTB_DATA_R&=~(pins_mask);
			else
				GPIO_PORTB_DATA_R|=(pins_mask);
		break;
		
		
	case 2: // if port C	
	if(pins_level == STD_LOW)
		 GPIO_PORTC_DATA_R&=~(pins_mask);
			else
				GPIO_PORTC_DATA_R|=(pins_mask);
	break;	
	
	
	
	case 3: // if port D
	if(pins_level == STD_LOW)
		 GPIO_PORTD_DATA_R&=~(pins_mask);
			else
				GPIO_PORTD_DATA_R|=(pins_mask);
	break;	
	
	
	case 4: // if port E
	if(pins_level == STD_LOW)
		 GPIO_PORTE_DATA_R&=~(pins_mask);
			else
				GPIO_PORTE_DATA_R|=(pins_mask);
	break;
	
	
	case 5: // if port F
	if(pins_level == STD_LOW)
		 GPIO_PORTF_DATA_R&=~(pins_mask);
	else
		 GPIO_PORTF_DATA_R|=pins_mask;
	break;
}
}
uint8_t   DIO_ReadPort(uint8_t port_index, uint8_t pins_mask)
{
	 

	switch(port_index){
		case 0 : // if port A
		return GPIO_PORTA_DATA_R&pins_mask;
		break;
		
		
		case 1: // if port B
		return GPIO_PORTB_DATA_R&pins_mask;
		break;
		
		
	case 2: // if port C	
	return GPIO_PORTC_DATA_R&pins_mask;
	break;	
	
	
	
	case 3: // if port D
	return GPIO_PORTD_DATA_R&pins_mask;
	break;	
	
	
	case 4: // if port E
	return GPIO_PORTE_DATA_R&pins_mask;
	break;
	
	
	case 5: // if port F
	return GPIO_PORTF_DATA_R&pins_mask;
	break;
}
}
