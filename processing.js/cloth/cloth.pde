int cols, rows;
int scl = 10;
int w = 1000;
int h = 2000;

float[][] terrain;

float flying = 0;

void setup() {
  size(600,600, P3D);
  cols = w / scl;
  rows = h / scl;
  terrain = new float[cols][rows];
  
  //frameRate(20);
}

void draw() {
  flying -= 0.1;
  float yoff = flying;
  for (int y = 0; y < rows; y++ ) {
    float xoff = 0;
    for (int x = 0; x < cols; x++ ) {
      terrain[x][y] = map(noise(xoff, yoff), 0, 1, -150, 150) ;
      xoff += 0.01;
    }
    yoff += 0.05;
    // 0.01 is flat, 0.1 is rolling, 0.05 is water/sand
  } 
  
  //background(0);
  background(254,166,33,75);
  
  stroke(255, 70, 0, 10);
  noFill();
  //fill(255,70,20);
  
  translate(width/2, height/2+50);
  rotateX(PI/3);
  rotateZ(PI/2);
  rotateZ(radians(frameCount*0.03));
  translate(-w/2, -h/2);


  for (int y = 0; y < rows - 1; y++ ) {
    beginShape(TRIANGLE_STRIP);
    for (int x = 0; x < cols; x++ ) {
      vertex(x*scl, y*scl, terrain[x][y]);
      vertex(x*scl, (y+1)*scl, terrain[x][y+1]);
      //rect(x*scl, y*scl, scl, scl); 
    }
    endShape();
  }
}