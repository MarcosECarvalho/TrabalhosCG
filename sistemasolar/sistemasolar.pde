

void setup() {
  size(400,400);
  background(0,0,0);
  ellipseMode(CENTER); //modificar a origem da elipse
}
void sol(){
  fill(255,255,0,100);
  circle(0,0,150);
}

void terra(){
  fill(0,255,200,100);
  circle(0,0,10);
}

void lua(){
  translate(width/30,0); //deslocar o eixo da lua em relacao a uma parte do eixo da terra
  fill(255,255,255,100);
  circle(0,0,5);
}

void draw() {
    background(200);
    translate(width/2, height/2);  
    pushMatrix();
    sol(); 
    popMatrix();
    pushMatrix();
    rotate(frameCount/(40*TWO_PI));  
    translate(width/3,0);   
    terra();
    rotate(frameCount/(40*TWO_PI)); 
    pushMatrix();
    lua();
    popMatrix();
    popMatrix();

}
