#include "nu32dip.h" // constants, functions for startup and UART
#include "stdio.h"
#include "math.h"
void blink(int, int); // blink the LEDs function

int main(void) {

 
  int i;
  char message[100];
  
  NU32DIP_Startup(); // cache on, interrupts on, LED/button init, UART init
  while (1) {
    
  
	if (PORTAbits.RA4 ==0){
        int i =0;
        for(i=0;i<100;i++){
            sprintf(message,"%f\r\n",sin(i*6.28/100.0));
            NU32DIP_WriteUART1(message);
            _CP0_SET_COUNT(0);
            while(_CP0_GET_COUNT()<240000){}
    }
  
  _CP0_SET_COUNT(0);
  while(_CP0_GET_COUNT()<24000000*5){}
    }     
        
}
}
  

// blink the LEDs
void blink(int iterations, int time_ms){
	int i;
	unsigned int t;
	for (i=0; i< iterations; i++){
		NU32DIP_GREEN = 0; // on
		NU32DIP_YELLOW = 1; // off
		t = _CP0_GET_COUNT(); // should really check for overflow here
		// the core timer ticks at half the SYSCLK, so 24000000 times per second
		// so each millisecond is 24000 ticks
		// wait half in each delay
		while(_CP0_GET_COUNT() < t + 12000*time_ms){}
		
		NU32DIP_GREEN = 1; // off
		NU32DIP_YELLOW = 0; // on
		t = _CP0_GET_COUNT(); // should really check for overflow here
		while(_CP0_GET_COUNT() < t + 12000*time_ms){}
	}
}
		