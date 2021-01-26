from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO


# Reads the Genome file
record = SeqIO.read("Genome.gb", "genbank")

# Creates new blank diagram and sets feature name
gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# Assigns colors for the feature
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(gd_feature_set) % 3 == 0:
        color = colors.red
    elif len(gd_feature_set) % 3 == 1:
        color = colors.blue
    else:
        color = colors.green

    # Assigns all feature to the a feature set
    gd_feature_set.add_feature(feature, sigil="JAGGY",
                               arrowshaft_height=0.9,color=color, label=True,
                               label_size=14, label_angle=0,)
    # draws all the feature
    gd_diagram.draw(format="circular", circular=True, pagesize=(20 * cm, 20 * cm),
                   start=0, end=len(record), circle_core=0.7)
    # Prints the graph
    gd_diagram.write("arrow_plasmid_circular.pdf", "PDF")