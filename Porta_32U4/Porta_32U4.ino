//|  0xAA  |  FUN  |  N_PARA   | PARA_1  | PARA_2  | ...  |  PARA_N  |  0xBB, 0xCC, 0xDD  |

#define N_AZIONI 1
#define PIN 7

typedef struct azione {
  unsigned char command;
  byte nPara;
  void (*action)();
} azione;

azione azioni[N_AZIONI];

void fun1()
{
  digitalWrite(PIN, HIGH);
  delay(500);
  digitalWrite(PIN, LOW);

}



void setup() {
  Serial.begin(115200);
  pinMode(PIN, OUTPUT);

  azioni[0].command = 0x01;
  azioni[0].nPara = 1;
  azioni[0].action = fun1;


  Serial1.begin(115200);

  Serial.println("Buongiorno!");

}

void loop() {

  if (Serial1.available() && Serial1.read() == 0xAA)
  {
    Serial.println("Entrato");
    byte command = Serial1.read();
    byte nPara = Serial1.read();
    byte trovato = 0;
    byte corretto = 0;
    int i;

    byte *para = (byte *)malloc(nPara * sizeof(byte));

    for (int j = 0; j < nPara; j++)
      para[j] = Serial1.read();

    if (Serial1.read() == 0xBB && Serial1.read() == 0xCC && Serial1.read() == 0xDD)
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
        else if (!trovato && i >= N_AZIONI - 1)
          Serial.println("Comando non esistente!");
      }
    }
    else
      Serial.println("Frame non corretto!");
  }
  else {
    delay(500);
  }









}


