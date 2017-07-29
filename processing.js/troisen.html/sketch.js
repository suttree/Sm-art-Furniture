function setup() {
  createCanvas(windowWidth, windowHeight, P3D);
  background('#fea621');
}

function draw() {
  beginShape(TRIANGLE_STRIP);
  vertex(30, 20);
  vertex(85, 20);
  vertex(85, 75);
  vertex(30, 75);
  endShape(CLOSE);
}