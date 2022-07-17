#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3f, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); 


void welcome_mssg() 
{
lcd.setCursor(0,0);  
lcd.print("     Uilatech "); 
delay(1000);
lcd.clear();
lcd.setCursor(0,0);  
lcd.print("   Smart Garbage     ");
lcd.setCursor(0,1);
lcd.print("Disposal System");

delay(3000); 
}
void waiting_mssg()
{
 lcd.setCursor(0,0);
 lcd.print("system processing");
 lcd.setCursor(0,1);
 lcd.print("  Please wait ");
 delay(3000);
 lcd.clear();
 }
 
void access_granted()
{
 lcd.setCursor(0,0);
 lcd.print("  access granted ");
 delay(5000);
 lcd.clear();
 lcd.setCursor(0,1);
 lcd.print("insert garbage");
 delay(8000);
 lcd.clear();
 }
 
 void access_denied()
 {
  lcd.setCursor(0,0);
  lcd.print("  access denied  ");
  lcd.setCursor(0,1);
  lcd.print("card error");
  delay(5000);
  lcd.clear();
 }
 void plastic_detected()
 {
  lcd.setCursor(0,0);
  lcd.print("  plastic detected  ");
  delay(5000);
  lcd.clear();
 }
 void other_garbage()
 {
  lcd.setCursor(0,0);
  lcd.print("  plastic not detected  ");
  delay(5000);
  lcd.clear();
 }
 void transaction_mssg()
 {
  lcd.setCursor(0,0);
  lcd.print("  transaction processing  ");
  lcd.setCursor(0,1);
  lcd.print("please wait");
  delay(5000);
  lcd.clear();
 
 }
