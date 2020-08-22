#include "micro_config.h"
#include "lcd.h"
#include "logic.h"

void SystemInit(){
}

int main()
	{	
		systick_init();
		LCD_init();
		UART_Init(0);
		
		
		LCD_sendCommand(CURSOR_OFF);
		LCD_displayString ("State: ");
		while(1)
		{
			uint8_t state = UART_Read(0);
			
			if (state == 1)
			{
				LCD_displayString ("Focused");
			}
			else if (state == 2)
			{
				LCD_displayString ("Defocused");
			}
		  	else
			{
				LCD_displayString ("Drowsy");
			}
		}
		
	}