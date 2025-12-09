// Gmsh project created on Fri Oct 10 16:22:57 2025
SetFactory("OpenCASCADE");
//+
LARG  = 0.6;
LONG  = 3  ;
EPAIS = 0.05; 
POS   = LARG;
HAUT  = 0.4;
LB    = 0.1*LARG;
LH    = 1.1*LARG-LB;
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, LARG/2, 0, 1.0};
//+
Point(3) = {0, LARG/2, EPAIS, 1.0};
//+
Point(4) = {0, 0, EPAIS, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Extrude {3, 0, 0} { Surface{1}; }
//+
Point(9) = {POS, 0, 0, 1.0};
//+
Point(10) = {POS, LH/2, 0, 1.0};
//+
Point(11) = {POS, LB/2, -HAUT, 1.0};
//+
Point(12) = {POS, 0, -HAUT, 1.0};
//+
Line(13) = {9, 10};
//+
Line(14) = {10, 11};
//+
Line(15) = {11, 12};
//+
Line(16) = {12, 9};
//+
Curve Loop(7) = {14, 15, 16, 13};
//+
Plane Surface(7) = {7};
//+
Extrude {EPAIS, 0, 0} { Surface{7}; }
//+
BooleanUnion{ Volume{2}; Delete; }{ Volume{1}; Delete; }
//+
Fillet {1}{15, 14}{0.02}
//+
Physical Surface("SOCLE", 31) = {9};
//+
Physical Curve("SUPPORT", 32) = {12};
//+
Physical Surface("SYMETRIE", 33) = {1};
//+
Physical Volume("VOLT", 34) = {1};
