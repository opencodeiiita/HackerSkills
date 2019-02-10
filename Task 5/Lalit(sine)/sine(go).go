package main

import (
	"math"

	"github.com/Arafatk/glot"
)

func main() {
	dimensions := 2
	// The dimensions supported by the plot
	persist := false
	debug := false
	plot, _ := glot.NewPlot(dimensions, persist, debug)
	pointGroupName := "Sine Wave"
	var x []float64
	j := 0.0
	for i := 0; i < 10000; i++ {
		x = append(x, j)
		j += 0.0001
	}
	var y []float64
	for i := 0; i < 10000; i++ {
		y = append(y, math.Sin(x[i]*2*math.Pi))
	}
	style := "lines"
	points := [][]float64{x, y}
	plot.AddPointGroup(pointGroupName, style, points)
	plot.SetTitle("Sine Plot")
	plot.SetYrange(-2, 2)
	plot.SetXLabel("X-Axis(2* pi * x)")
	plot.SetYLabel("Y-Axis")
	plot.SavePlot("sine(go).png")
	
}