#include "port.h"


void Port_Init(uint8_t port_index){
	uint32_t delay;
  SYSCTL_RCGCGPIO_R  |= (1<<port_index);
	delay = 1;
	switch(port_index) {
		case 0 :// PORTA selected
	         GPIO_PORTA_LOCK_R = 0x4C4F434B;
	         GPIO_PORTA_CR_R= 0xFF;
	         GPIO_PORTA_AFSEL_R=0;
	         GPIO_PORTA_PCTL_R=0;
	         GPIO_PORTA_AMSEL_R=0;
	         GPIO_PORTA_DEN_R = 0xFF;
		       break;
		case 1 : //PORTB selected
				   GPIO_PORTB_LOCK_R = 0x4C4F434B;
	         GPIO_PORTB_CR_R= 0xFF;
	         GPIO_PORTB_AFSEL_R=0;
	         GPIO_PORTB_PCTL_R=0;
	         GPIO_PORTB_AMSEL_R=0;
	         GPIO_PORTB_DEN_R = 0xFF;
		       break ;
		case 2 : // PORTC selected
				   GPIO_PORTC_LOCK_R = 0x4C4F434B;
	         GPIO_PORTC_CR_R= 0xFF;
	         GPIO_PORTC_AFSEL_R=0;
	         GPIO_PORTC_PCTL_R=0;
	         GPIO_PORTC_AMSEL_R=0;
	         GPIO_PORTC_DEN_R = 0xFF;
		       break ;
		case 3 :  // PORTD selected
				   GPIO_PORTD_LOCK_R = 0x4C4F434B;
	         GPIO_PORTD_CR_R= 0xFF;
	         GPIO_PORTD_AFSEL_R=0;
	         GPIO_PORTD_PCTL_R=0;
	         GPIO_PORTD_AMSEL_R=0;
	         GPIO_PORTD_DEN_R = 0xFF;
		       break ;
		case 4 :  // PORTE selected
				   GPIO_PORTE_LOCK_R = 0x4C4F434B;
	         GPIO_PORTE_CR_R= 0x3F;
	         GPIO_PORTE_AFSEL_R=0;
	         GPIO_PORTE_PCTL_R=0;
	         GPIO_PORTE_AMSEL_R=0;
	         GPIO_PORTE_DEN_R = 0x3F;
		       break ;
		case 5 : { // PORTF selected
				   GPIO_PORTF_LOCK_R = 0x4C4F434B;
	         GPIO_PORTF_CR_R= 0x1F;
	         GPIO_PORTF_AFSEL_R=0;
	         GPIO_PORTF_PCTL_R=0;
	         GPIO_PORTF_AMSEL_R=0;
	         GPIO_PORTF_DEN_R = 0x1F;
		       break ;
		}
	}
}
	void Port_SetPinDirection(uint8_t port_index , uint8_t pins_mask , Port_PinDirectionType pins_direction) {
		switch(port_index) {
			
			case 0 : 
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTA_DIR_R |= pins_mask;
				else
					GPIO_PORTA_DIR_R &= (~pins_mask);
				break ;
			case 1 :
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTB_DIR_R |= pins_mask;
				else
					GPIO_PORTB_DIR_R &= (~pins_mask);
				break ;
				
			case 2 :
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTC_DIR_R |= pins_mask;
				else
					GPIO_PORTC_DIR_R &= (~pins_mask);
				break ;
			case 3 :
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTD_DIR_R |= pins_mask;
				else
					GPIO_PORTD_DIR_R &= (~pins_mask);
				break;
			case 4 :
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTE_DIR_R |= pins_mask;
				else
					GPIO_PORTE_DIR_R &= (~pins_mask);
				break;
			case 5 : 
				if(pins_direction==PORT_PIN_OUT)
				   GPIO_PORTF_DIR_R |= pins_mask;
				else
					GPIO_PORTF_DIR_R &= (~pins_mask);
				break ;
		}
	}
	void Port_SetPinPullUp( uint8_t port_index , uint8_t pins_mask ,uint8_t enable){
	switch(port_index){
	case 0 :
	if(enable==1){
    GPIO_PORTA_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTA_PUR_R &=(~pins_mask);
	}
	break;
	case 1:
	if(enable==1){
		GPIO_PORTB_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTB_PUR_R &=(~pins_mask);
	}
	break;
	case 2:
	if(enable==1){
		GPIO_PORTC_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTC_PUR_R &=(~pins_mask);
	}
	break;	
	case 3:
	if(enable==1){
		GPIO_PORTD_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTD_PUR_R &=(~pins_mask);
	}
	break;	
	case 4:
	if(enable==1){
		GPIO_PORTE_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTE_PUR_R &=(~pins_mask);
	}
	break;
	case 5:
	if(enable==1){
		GPIO_PORTF_PUR_R|=pins_mask;
	}
	else {
		GPIO_PORTF_PUR_R &=(~pins_mask);
	}
	break;
	}
}
void Port_SetPinPullDown
( uint8_t port_index , uint8_t pins_mask ,uint8_t enable){
	switch(port_index){// if port A
		case 0 :
			if(enable==1){
		GPIO_PORTA_PDR_R|=pins_mask; // MAKE ENABLE FOR PINS IN THE MASK
	}
	else {
		GPIO_PORTA_PDR_R &=(~pins_mask); // MAKE disable FOR PINS IN THE MASK
	}
	break;
		case 1: // if port B
			if(enable==1){
		GPIO_PORTB_PDR_R|=pins_mask; 
	}
	else {
		GPIO_PORTB_PDR_R &=(~pins_mask);
	}
	break;
	case 2: // if port C
			if(enable==1){
		GPIO_PORTC_PDR_R|=pins_mask;
	}
	else {
		GPIO_PORTC_PDR_R &=(~pins_mask);
	}
	break;	
	
	case 3: // if port D
			if(enable==1){
		GPIO_PORTD_PDR_R|=pins_mask;
	}
	else {
		GPIO_PORTD_PDR_R &=(~pins_mask);
	}
	break;	
	case 4: // if port E
			if(enable==1){
		GPIO_PORTE_PDR_R|=pins_mask;
	}
	else {
		GPIO_PORTE_PDR_R &=(~pins_mask);
	}
	break;
	case 5: // if port F
			if(enable==1){
		GPIO_PORTF_PDR_R|=pins_mask;
	}
	else {
		GPIO_PORTF_PDR_R &=(~pins_mask);
	}
	break;
	
	
	}

	
}