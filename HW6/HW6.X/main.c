#include "nu32dip.h" // constants, functions for startup and UART
#include "stdio.h"
#include "i2c_master_noint.h"

void blink();
void turnOFFGP7();
void turnONGP7();
int readGP0();

int main(){
    
    NU32DIP_Startup();// nu32 startup
    i2c_master_setup();//init the i2c pins
    
   
    
    
    
    
    while(1){
        int r;
         //init the chip, GP0 input, GP7 output
        i2c_master_start();
        i2c_master_send(0b01000000);
        i2c_master_send(0x00);
        i2c_master_send(0b01111111);
        i2c_master_stop();
        
        i2c_master_start();
        i2c_master_send(0b01000000);
        i2c_master_send(0x0A);
        i2c_master_send(0b00000000);
        i2c_master_stop();
        
        //blink the yellow LED in PIC
        //blink();
        //blink GP7 - to start
            // turn on GP7
            //delay
            // turn off GP7
            //delay
        //turnONGP7();
      
        //Once that works delete
        r = readGP0();
        //if(r)
        if(r){
            turnOFFGP7();
            
        }
        else{
            turnONGP7();    
        }
        
            //turn on GP7
        //else
            //turn off GP7
    }
}

void turnONGP7(){
    //send start bit - call start 
    i2c_master_start();
    //send the address of the chip
        //0b01000000 (0 to write)
    i2c_master_send(0b01000000);
    //send the register name
        //OLAT 0x0A 
    i2c_master_send(0x0A);
    //send the value to turn on GP7
        //0b10000000 - turn off gp0-6, on gp7
    i2c_master_send(0b10000000);
    //send the stop bit - call stop
    i2c_master_stop();
}

void turnOFFGP7(){
     //send start bit - call start 
    i2c_master_start();
    //send the address of the chip
        //0b01000000 (0 to write)
    i2c_master_send(0b01000000);
    //send the register name
        //OLAT 0x0A 
    i2c_master_send(0x0A);
    //send the value to turn on GP7
        //0b10000000 - turn off gp0-6, on gp7
    i2c_master_send(0b00000000);
    //send the stop bit - call stop
    i2c_master_stop();
}
int readGP0(){
    //send start bit - call start
    i2c_master_start();
    // send address with write bit
        //0b01000000
    i2c_master_send(0b01000000);
    //send register you want to read from 
    i2c_master_send(0x09);
    //restart
    i2c_master_restart();
    //send address with read bit
        //0b01000001
    i2c_master_send(0b01000001);
    unsigned char a = i2c_master_recv();
    //send the ACK bit
    i2c_master_ack(1);
    //send the stop bit
    i2c_master_stop();
    return (a<<7);
}
void blink(){
	int i;
	unsigned int t;
	for (i=0; i< 5; i++){
		 // on
		NU32DIP_YELLOW = 1; // off
		t = _CP0_GET_COUNT(); // should really check for overflow here
		// the core timer ticks at half the SYSCLK, so 24000000 times per second
		// so each millisecond is 24000 ticks
		// wait half in each delay
		while(_CP0_GET_COUNT() < t + 12000*1000){}
		
		 // off
		NU32DIP_YELLOW = 0; // on
		t = _CP0_GET_COUNT(); // should really check for overflow here
		while(_CP0_GET_COUNT() < t + 12000*1000){}
	}
}