from simpful import *


FS = FuzzySystem()

# Defining track temperature (in degrees celcius)
temp1 = FuzzySet(points=[[10., 1.],  [30., 0.]], term="cold")
temp2 = FuzzySet(points=[[25., 0.], [35., 1.], [50., 0.]], term="avg")
temp3 = FuzzySet(points=[[45., 0.],  [70., 1.]], term="hot")
FS.add_linguistic_variable("TrackTemp", LinguisticVariable([temp1, temp2, temp3], concept="Track temperature"))

# Defining tire compound hardness (enumurated types)
comp1 = FuzzySet(points=[[0., 0.], [1., 1.], [2., 0.]], term="soft")
comp2 = FuzzySet(points=[[1., 0.], [2., 1.], [3., 0.]], term="med")
comp3 = FuzzySet(points=[[2., 0.], [3., 1.], [4., 0.]], term="hard")
comp4 = FuzzySet(points=[[3., 0.], [4., 1.], [5., 0.]], term = "wet")
FS.add_linguistic_variable("Compound", LinguisticVariable([comp1, comp2, comp3, comp4], concept="Tire compound"))

# Defining weather (in decimeters (.1 of mm) of precipitation)
rain1 = FuzzySet(points=[[0., 1.],  [10., 0.]], term="dry")
rain2 = FuzzySet(points=[[5., 0.], [13., 1.], [20., 0.]], term="damp")
rain3 = FuzzySet(points=[[15., 0.],  [30., 1.]], term="wet")
FS.add_linguistic_variable("Weather", LinguisticVariable([rain1, rain2, rain3], concept="Weather"))

# Defining current tire lifespan (in laps)
laps1 = FuzzySet(points=[[0., 1.],  [10., 0.]], term="new")
laps2 = FuzzySet(points=[[8., 0.], [15., 1.], [20., 0.]], term="aging")
laps3 = FuzzySet(points=[[18., 0.],  [25., 1.], [30., 0.]], term="old")
laps4 = FuzzySet(points=[[28., 0], [32., 1]], term="dead")
FS.add_linguistic_variable("Lifespan", LinguisticVariable([laps1, laps2, laps3, laps4], concept="Lifespan"))

# Defining recommendation value (0-100)
FS.set_crisp_output_value("none", 0)
FS.set_crisp_output_value("low", 25)
FS.set_crisp_output_value("med", 50)
FS.set_crisp_output_value("high", 75)
FS.set_crisp_output_value("crit", 100)

# Define rules regarding track temperature
r1 = "IF (TrackTemp IS cold) THEN (Rec IS low)"
r2 = "IF (TrackTemp IS avg) THEN (Rec IS med)"
r3 = "IF (TrackTemp IS hot) THEN (Rec IS high)"

# Define rules regarding weather
r4 = "IF (Weather IS dry) AND (Compound IS wet) THEN (Rec IS crit)"
r5 = "IF (Weather IS damp) AND (Compound IS wet) THEN (Rec IS med)"
r6 = "IF (Weather IS wet) AND (Compound IS wet) THEN (Rec IS none)"
r7 = "IF (Weather IS wet) AND (NOT (Compound IS wet)) THEN (Rec IS crit)"
r8 = "IF (Weather IS damp) AND (NOT (Compound IS wet)) THEN (Rec IS med)"

# Define rules regarding lifespan
r9 = "IF (Lifespan IS new) THEN (Rec IS none)"
r10 = "IF (Compound IS soft) AND (Lifespan IS aging) THEN (Rec IS med)"
r11 = "IF (Compound IS soft) AND (Lifespan IS old) THEN (Rec IS high)"
r12 = "IF (Compound IS soft) AND (Lifespan IS dead) THEN (Rec IS crit)"
r13 = "IF (Compound IS med) AND (Lifespan IS aging) THEN (Rec IS low)"
r14 = "IF (Compound IS med) AND (Lifespan IS old) THEN (Rec IS med)"
r15 = "IF (Compound IS med) AND (Lifespan IS dead) THEN (Rec IS high)"
r16 = "IF (Compound IS hard) AND (Lifespan IS aging) THEN (Rec IS none)"
r17 = "IF (Compound IS hard) AND (Lifespan IS old) THEN (Rec IS med)"
r18 = "IF (Compound IS hard) AND (Lifespan IS dead) THEN (Rec IS high)"
r19 = "IF (Compound IS wet) THEN (Rec IS high)"

FS.add_rules([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19])


# Acquire values from user
print("Track temperature (degrees Celcius):  ")
FS.set_variable("TrackTemp", int(input()))

print("Weather (decimeters of precipitation):  ")
FS.set_variable("Weather", int(input()))

print("Current tire age (in laps):  ")
FS.set_variable("Lifespan", int(input()))

print("Tire compound (soft, med, hard, or wet):  ")

comp = str(input())
if (comp == "soft"):
    FS.set_variable("Compound", 1)
elif (comp == "med"):
    FS.set_variable("Compound", 2)
elif (comp == "hard"):
    FS.set_variable("Compound", 3)
elif (comp == "wet"):
    FS.set_variable("Compound", 4)


# Print output
print(FS.Sugeno_inference(["Rec"]))