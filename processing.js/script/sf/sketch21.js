var xOffset = 0;       // Perlin x-offset
var yOffset = 0;       // Perlin y-offset
var offsetInc = 0.006; // Perlin offset increment
var inc = 1;           // Perin increment
var s = 1;             // Start size of perlin ring
var m = 1.005;         // Size multiplier

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  blendMode(ADD);
  noFill();
  stroke(255, 64, 8, 128);
}

function draw() {
  translate(width * 0.5, height * 0.5);

  if (s < 2000) {
    // Create a series of perlin rings from big to small
    for (var nTimes = 0; nTimes < 10; nTimes++) {

      // Less points for smaller rings
      nPoints = int(2 * PI * s);
      nPoints = min(nPoints, 500);

      // Create ring
      beginShape();
      for (var i = 0; i < nPoints; i++) {
        var a = i / nPoints * TAU;
        var p = p5.Vector.fromAngle(i / nPoints * TAU);
        var n = noise(xOffset + p.x * inc, yOffset + p.y * inc) * s;
        p.mult(n);
        vertex(p.x, p.y);
      }
      endShape(CLOSE);

      // Increment perlin offset for next ring
      xOffset += offsetInc;
      yOffset += offsetInc;

      // Reduce size for next ring
      s *= m;
    }
  } else {
    noLoop();
  }
}
