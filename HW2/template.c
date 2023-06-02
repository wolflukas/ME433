#include "nu32dip.h" // constants, functions for startup and UART

void blink(int, int); // blink the LEDs function

int main(void) {
  char message[100];
  char message2[100];
  int iter =0;
  int ti=0;
  
  NU32DIP_Startup(); // cache on, interrupts on, LED/button init, UART init
  while (1) {
    NU32DIP_ReadUART1(message, 100); // wait here until get message from computer
    NU32DIP_WriteUART1(message); // send message back
    sscanf(message, "%d", &iter);
    NU32DIP_ReadUART1(message2, 100);
    NU32DIP_WriteUART1(message2); // carriage return and newline
    sscanf(message2, "%d", &ti);
	if (NU32DIP_USER){
		blink(iter, ti); // 5 times, 500ms each time
	} 
    if (PORTBbits.RB4 == 0){ //if the B4 button is pressed, then we we will blink A4.
            

    _CP0_SET_COUNT(0);
    int ctime = _CP0_GET_COUNT();   //This will get the current count -- the core time is 32-bit timer.

    while (ctime != NU32DIP_DESIRED_BAUD ){

        ctime = _CP0_GET_COUNT();   //This will get the current count -- the core time is 32-bit timer.

        if (ctime < 12000000){
            LATAbits.LATA4 = 1; //Turn the A4 bit on 
        }
        else if (ctime >= 12000000 && ctime < 24000000){
            LATAbits.LATA4 = 0;     //Turn the A4 bit off. 
        }
        else if (ctime >= 24000000 && ctime < 36000000){    
            LATAbits.LATA4 = 1;     //Turn the A4 bit on 
        }  
        else if (ctime >= 36000000){
            LATAbits.LATA4 = 0;
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
		
