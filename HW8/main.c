#include "font.h"
#include "i2c_master_noint.h"
#include "mpu6050.h"
#include "nu32dip.h"
#include "ssd1306.h"

void blink(int, int); 
void drawChar(char, char, char);
void drawString(char*, char, char);

int main(void) {
    NU32DIP_Startup(); // cache on, interrupts on, LED/button init, UART init
    init_mpu6050(); 
    ssd1306_setup();
    unsigned char d[14];
    float az;
    //char* input;
    char input[100];
    int count;
    float count2;
    char count3[100];
   
    
    while(1){
        _CP0_SET_COUNT(0);
        blink(1, 5);

        // read IMU
        burst_read_mpu6050(d);
		// convert data
      
        az = conv_zXL(d);
        sprintf(input,"%f\r\n",az);
        

        // print out the data (ax, ay, or any of the other floats)
        
        ssd1306_update();
        //drawString(input,0,0);
        //ssd1306_drawPixel(50,10,1);
        //char input = 'A';
        //drawChar(input, 50, 10);
        //char* input2 = "hello!";
        drawString(input,0,0);
        count = _CP0_GET_COUNT();
        count2 = 12000000/count;
        sprintf(count3, "%f\r\n", count2);
        drawString(count3, 0, 20);
        
    }
}


void drawChar(char letter, char x, char y){
    int j;
    int i;
    for (j = 0; j<5; j++){
        char col = ASCII[letter-0x20][j];
        for (i=0;i<8;i++){
            ssd1306_drawPixel(x+j,y+i, (col>>i)&0b1);
        }
    }
}
void drawString(char*m, char x, char y){//m char*
    int k=0;
    while(m[k]!=0){
        drawChar(m[k],x+5*k,y);
        k++;
    }
}

void blink(int iterations, int time_ms) {
    int i;
    unsigned int t;
    for (i = 0; i < iterations; i++) {
        NU32DIP_GREEN = 0; // on
        NU32DIP_YELLOW = 1; // off
        t = _CP0_GET_COUNT(); // should really check for overflow here
        // the core timer ticks at half the SYSCLK, so 24000000 times per second
        // so each millisecond is 24000 ticks
        // wait half in each delay
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {
        }

        NU32DIP_GREEN = 1; // off
        NU32DIP_YELLOW = 0; // on
        t = _CP0_GET_COUNT(); // should really check for overflow here
        while (_CP0_GET_COUNT() < t + 12000 * time_ms) {
        }
    }
}
