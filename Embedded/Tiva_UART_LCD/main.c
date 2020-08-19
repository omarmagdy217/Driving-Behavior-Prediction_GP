#include "micro_config.h"
#include "lcd.h"
#include "logic.h"

void SystemInit(){
}

int main()
	{
		//uint8_t delay=0;
		// Delete probably
		//Port_Init(0);
		//Port_SetPinDirection(0 , 0xFC , PORT_PIN_OUT);
   	//Port_SetPinPullUp( 1 , 0xFF ,1);
		//DIO_WritePort(5, 0x0E, STD_LOW);
		//DIO_WritePort(0, 0xFF, STD_HIGH);
		
		systick_init();
		//_delay_ms(500);
		//LCD_init();
		UART_Init(7);
		
		//Port_SetPinDirection(0 , 0x0C , PORT_PIN_OUT);
		//DIO_WritePort(0, 0x0C, STD_LOW);
		//_delay_ms(500);
		//LCD_sendCommand(CURSOR_OFF);
		//LCD_displayString ("ya rab");
		//_delay_ms(500);
	  //LCD_displayCharacter(0);
		
		//LCD_intgerToString(5);
		
		while(1)
		{
			//LCD_intgerToString(UART_Read(0));
			//uint8_t state = UART_Read(0);
			//LCD_displayCharacter(state);
			//_delay_ms(2000);
			//LCD_displayString ("Here");
			//LCD_clearScreen();
			UART_Write(7,'0');
			//UART_sendString("\n\r\n\r");		
			//UART_sendString("Select an LED color:\n\r");
			//UART_sendString("1) Black (OFF)\n\r");
			//UART_sendString("2) Blue\n\r");
			
			//_delay_ms(100);
			/*if (state == 0)
			{
				DIO_WritePort(0, 0x04, STD_HIGH);
				DIO_WritePort(0, 0x08, STD_LOW);
				//UART_Write(7,state);
				//UART_sendString("\n\r\n\r");		
				//UART_sendString("Select an LED color:\n\r");
			}
			else if (state == 1)
			{
				DIO_WritePort(0, 0x08, STD_HIGH);
				DIO_WritePort(0, 0x04, STD_LOW);
			}
		  */
			//_delay_ms(100);
			//LCD_intgerToString(UART_Read(7));
			// Read state from putty
			//uint8_t state = UART_Read(7);
			// Write to LCD
			//output(state);
			// Send contol script to putty
			//UART_sendString(&state);
		}
		
	}