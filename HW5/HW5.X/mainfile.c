#include <proc/p32mx170f256b.h>

#include "nu32dip.h"
#include "spi.h"
#include "stdio.h"
#include "math.h"





int main(void){
    NU32DIP_Startup();
    initSPI();
    int i;
    float value;
    unsigned int signwave;
    unsigned short t=0b0000000000000000;
    unsigned short plus = 0b0000000000000000;
    unsigned short a_or = 0;
    unsigned short a_orp = 0;
    unsigned int tri;
    while(1){
        //voltage for sin
        for(i=0;i<200;i++){
                _CP0_SET_COUNT(0);
                LATAbits.LATA0 =0;
                a_or =0;
                t = 0b0111000000000000;
                t=t|(a_or<<15);
                signwave = 1023/2*sin(i*6.28/200)+(1023/2);
                t = t|(signwave<<2);
                spi_io(t>>8);
                spi_io(t);
                LATAbits.LATA0=1;
                LATAbits.LATA0=0;
                if(i % 2 ==0){
                    a_orp = 1;
                    if(i<101){
                        tri = i*(1023/100);
                    }
                    else{
                        tri = (100-(i-100))*(1023/100);
                    }
                    plus = 0b1111000000000000;
                    plus=plus|(a_orp<<15);
                    plus=plus|(tri<<2);
                
                    spi_io(plus>>8);
                    spi_io(plus);
                
                }
            
            LATAbits.LATA0 =1;
            
            
            while(_CP0_GET_COUNT()<6000) {}       
                
        }
        
        //send to spi
        
        //voltage for tri
        //send to spi
        
        //delay
    }
    
}

       