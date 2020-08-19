#ifndef LCD_H_
#define LCD_H_

#include "micro_config.h"

/*******************************************************************************
 *                      Preprocessor Macros                                    *
 *******************************************************************************/
/* LCD HW Pins */
#define RS 0x20
#define RW 0x40
#define E  0x80
#define LCD_CTRL_PORT 0				
#define LCD_DATA_PORT GPIO_PORTB_DATA_R

/* LCD Commands */
#define CLEAR_COMMAND 0x01
#define TWO_LINE_LCD_Eight_BIT_MODE 0x38
#define CURSOR_OFF 0x0C
#define CURSOR_ON 0x0E
#define SET_CURSOR_LOCATION 0x80 

/*******************************************************************************
 *                      Functions Prototypes                                   *
 *******************************************************************************/
 
void LCD_sendCommand(uint8_t command);
void LCD_displayCharacter(uint8_t data);
void LCD_displayString(const char *Str);
void LCD_init(void);
void LCD_clearScreen(void);
void LCD_displayStringRowColumn(uint8_t row,uint8_t col,const char *Str);
void LCD_goToRowColumn(uint8_t row,uint8_t col);
void LCD_intgerToString(uint32_t data);
void _delay_ms(uint32_t y);

#endif /* LCD_H_ */