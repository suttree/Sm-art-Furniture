function setup() {
	createCanvas(1024,768);
	background(100);
}

function draw() {
	/*
	strokeWeight(1);
	ellipse(50, 50, 100, 100);
	rect(10, 10, 90, 90);
	rect(20, 20, 70, 70);
	line(0, 0, 500, 500);
	strokeWeight(10);
	line(0, 500, 500, 0);
	ellipse(200, 500, 200, 100);
	*/

	strokeWeight(10);
	
	stroke(0);
	//fill(255, 0, 0);
	noFill();
	rect(100, 100, 300, 300);
	
	stroke(0, 255, 255);
	fill(255, 255, 0, 200);
	rect(250, 250, 300, 300);
	
	fill(200, 100);
	//stroke(255, 0, 0, 100);
	noStroke();
	rect(150, 150, 300, 300);
}
