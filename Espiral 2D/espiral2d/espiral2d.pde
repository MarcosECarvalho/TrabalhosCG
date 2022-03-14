int pv = 500; //pontos por volta
float a = TWO_PI/pv; 
int nv = 5; //numero de voltas
float theta; //coordenada angular
float r; //raio

void setup(){
size(300,300);
background(255,255,255);
}

void draw(){
translate(width/2, height/2);

beginShape(); 
//baseado no pseudocódigo fornecido em aula
  for(int v = 0; v < nv; v++){
    for(int p = 0; p < pv; p++){
      theta = (TWO_PI*v) + (p * a);
      r = v + theta * 4; //r = a + bθ equação de raio que incrimenta a cada interação, 5 foi arbitrário para incrementar a diferença de raio
      vertex(r*cos(theta), r*sin(theta));
    }
  }

endShape();

}
