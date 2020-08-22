#include "systick.h"


void systick_init(void){
	NVIC_ST_CTRL_R &= ~NVIC_ST_CTRL_ENABLE;
	NVIC_ST_RELOAD_R = NVIC_ST_RELOAD_M;
	NVIC_ST_CURRENT_R = NVIC_ST_CURRENT_S;
	NVIC_ST_CTRL_R |= (NVIC_ST_CTRL_CLK_SRC | NVIC_ST_CTRL_ENABLE);
}

void systick_wait(uint32_t delay){
	NVIC_ST_RELOAD_R = delay - 1;
	NVIC_ST_CURRENT_R = 0;
	while((NVIC_ST_CTRL_R&0x10000) == 0);
}
 void _delay_ms(uint32_t time){
	uint32_t i;
	for(i = 0;i < time;i++){
		systick_wait(80000);
	}
} 
