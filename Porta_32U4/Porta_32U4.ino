//|  0xAA  |  FUN  |  N_PARA   | PARA_1  | PARA_2  | ...  |  PARA_N  |  0xBB, 0xCC, 0xDD  |

#define N_AZIONI 3

typedef struct azione {
  unsigned char command;
  byte nPara;
  void (*action)();
} azione;

azione azioni[N_AZIONI];

void fun1()
{
  digitalWrite(13, HIGH);
}

void fun2()
{
  digitalWrite(13, LOW);
}

void fun3()
{
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}

void setup() {
  pinMode(13, OUTPUT);

  azioni[0].command = 0x01;
  azioni[0].nPara = 1;
  azioni[0].action = fun1;

  azioni[1].command = 0x02;
  azioni[1].nPara = 1;
  azioni[1].action = fun2;

  azioni[2].command = 0x03;
  azioni[2].nPara = 1;
  azioni[2].action = fun3;

  Serial.begin(9600);

  Serial.println("Buongiorno!");

}

void loop() {

  if (Serial.available() && Serial.read() == 0xAA)
  {
    byte command = Serial.read();
    byte nPara = Serial.read();
    byte trovato = 0;
    byte corretto = 0;
    int i;


    byte *para = (byte *)malloc(nPara * sizeof(byte));

    for (int j = 0; j < nPara; j++)
      para[j] = Serial.read();

    if (Serial.read() == 0xBB && Serial.read() == 0xCC && Serial.read() == 0xDD)
    {
      for (i = 0; i < N_AZIONI && !trovato; i++)
      {
        if (azioni[i].command == command && azioni[i].nPara == nPara)
        {
          trovato = 1;
          Serial.print("Ho ricevuto il dato ");
          Serial.println(command);

          Serial.print("N parametri = ");
          Serial.println(nPara, DEC);

          azioni[i].action();

          free(para);
        }
        else if (!trovato && i>=N_AZIONI-1)
          Serial.println("Comando non esistente!");
      }
    }
    else
      Serial.println("Frame non corretto!");
  }










}


