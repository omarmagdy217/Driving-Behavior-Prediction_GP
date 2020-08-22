#include "lcd.h"
#include "port.h"
#include "dio.h"
#include "micro_config.h"
void LCD_init(void)        // Function to initialise the LCD
{
	  Port_Init(0);
	  Port_Init(1);
	  Port_SetPinDirection(1,0xFF,PORT_PIN_OUT);
	  Port_SetPinDirection(0,0xE0,PORT_PIN_OUT);
    LCD_sendCommand(TWO_LINE_LCD_Eight_BIT_MODE);      // initialization of 16X2 LCD in 8bit mode
    LCD_sendCommand(CURSOR_OFF);      // cursor off
	  LCD_sendCommand(CLEAR_COMMAND);
}
void LCD_sendCommand(uint8_t command)
{
	DIO_WritePort(LCD_CTRL_PORT,RS,STD_LOW); /* Instruction Mode RS=0 */
	DIO_WritePort(LCD_CTRL_PORT,RW,STD_LOW); /* write data to LCD so RW=0 */
	_delay_ms(1); /* delay for processing Tas = 50ns */
	DIO_WritePort(LCD_CTRL_PORT,E,STD_HIGH); /* Enable LCD E=1 */
	_delay_ms(1); /* delay for processing Tpw - Tdws = 190ns */
	LCD_DATA_PORT = command; /* out the required command to the data bus D0 --> D7 */
	_delay_ms(1); /* delay for processing Tdsw = 100ns */
	DIO_WritePort(LCD_CTRL_PORT,E,STD_LOW);
	_delay_ms(1);

}
void LCD_displayCharacter(uint8_t data)
{
	DIO_WritePort(LCD_CTRL_PORT,RS,STD_HIGH); // RS pin is on PB1
	DIO_WritePort(LCD_CTRL_PORT,RW,STD_LOW); // R/W pin is on PB0
	_delay_ms(1); /* delay for processing Tas = 50ns */
		DIO_WritePort(LCD_CTRL_PORT,E,STD_HIGH); /* Enable LCD E=1 */
	_delay_ms(1);
		LCD_DATA_PORT = data; /* out the required data char to the data bus D0 --> D7 */
	_delay_ms(1); /* delay for processing Tpw - Tdws = 190ns */
			DIO_WritePort(LCD_CTRL_PORT,E,STD_LOW);
	_delay_ms(1); /* delay for processing Tdsw = 100ns */
	
}

char* itoa1(int i, char b[])
{
    char const digit[] = "0123456789";
    char* p = b;
	 int shifter = i;
    if(i<0){
        *p++ = '-';
        i *= -1; }
    do{ //Move to where representation ends
        ++p;
        shifter = shifter/10;
    }while(shifter);
    *p = '\0';
    do{ //Move back, inserting digits as u go
        *--p = digit[i%10];
        i = i/10;
    }while(i);
    return b;
}

void LCD_intgerToString(uint32_t data)
{
    char string [32];
    itoa1(data,string);
	  LCD_displayStringRowColumn(1,0 , string);
	
}
void LCD_clearScreen(void)
{
	LCD_sendCommand(CLEAR_COMMAND); //clear display 
}
void LCD_displayString(const char *Str)
{
	uint8_t i = 0;
	while(Str[i] != '\0')
	{
		LCD_displayCharacter(Str[i]);
		i++;
	}
	/***************** Another Method ***********************
	while((*Str) != '\0')
	{
		LCD_displayCharacter(*Str);
		Str++;
	}		
	*********************************************************/
}
void LCD_goToRowColumn(uint8_t row,uint8_t col)
{
	uint8_t Address;
	
	/* first of all calculate the required address */
	switch(row)
	{
		case 0:
				Address=col;
				break;
		case 1:
				Address=col+0x40;
				break;
		case 2:
				Address=col+0x10;
				break;
		case 3:
				Address=col+0x50;
				break;
	}					
	/* to write to a specific address in the LCD 
	 * we need to apply the corresponding command 0b10000000+Address */
	LCD_sendCommand(Address | SET_CURSOR_LOCATION); 
}
void LCD_displayStringRowColumn(uint8_t row,uint8_t col,const char *Str)
{
	LCD_goToRowColumn(row,col); /* go to to the required LCD position */
	LCD_displayString(Str); /* display the string */

}