#include "tm4c123gh6pm.h"
#include "Common_Macros.h"
#include "Can_PBcfg.h"

/*
	CAN0Rx PB4
	CAN0Tx PB5
*/

void CAN_REG_INIT ()
{
	SYSCTL_RCGC0_R = 0x01000000;		// Enable Can0 clock gating
	SYSCTL_RCGC2_R = 0x00000002;		// Enable PORTB clock gating
	GPIO_PORTB_AFSEL_R = 0x00000030;	// Enable pin alternate functions for PB4, PB5
	GPIO_PORTB_PCTL_R = 0x00880000;		// Configure CAN0 for pins PB4, PB5

	CAN0_CTL_R = 0x00000041;			// Set INIT, CCE bit
	CAN0_BIT_R = 0;
	CAN0_BIT_R = 	canConfigSet->canController->canControllerBaudrateConfig->CanControllerSeg2 << 12 |
					canConfigSet->canController->canControllerBaudrateConfig->CanControllerSeg1 << 8  |
					canConfigSet->canController->canControllerBaudrateConfig->CanControllerSyncJumpWidth << 6  |
					canConfigSet->canController->canControllerBaudrateConfig->CanControllerPropSeg;
	CLEAR_BIT(CAN0_IF1ARB2_R, 15);		// CHECK // Ignore msg object for init MSGVAL = 0
	
	/* INITIALIZE MSG OBJECTS */
	/* Transmit Message Object */
	CAN0_IF1CMSK_R = 0x00000086;		// Bit6,5,4 = 0 .. Bit2= 1        check
	CAN0_IF1MSK2_R = 0;          		// Disable filtering for transmission 

	CAN0_IF1ARB2_R = 0x0000A01C;		// ID[12:2] = 7
	SET_BIT(CAN0_IF1MCTL_R, 7);			// EOB = 1
	SET_BIT(CAN0_IF1MCTL_R, 3);			// DLC = 8

	SET_BIT(CAN0_IF1ARB2_R, 15);		// MSGVAL = 1
	CAN0_BRPE_R = 0;					// CHECK // Baud Rate Prescaler Extension
	CLEAR_BIT(CAN0_CTL_R, 0);			// Clear INIT bit
}

void CAN_REG_WRITE (data)
{
	CAN0_IF1CMSK_R = 0x00000083;		// WRNRD, DATAA, DATAB = 1
	CAN0_IF1DA1_R = data;				// Assign data
	CAN0_IF1CRQ_R = 0x00000001;			// MSG NUM = 1
	CAN0_IF1MCTL_R = 0x00008100; 		// Set TXRQST, NEWDAT
}