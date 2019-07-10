from biologicalgraphs.utilities import dataIO
from biologicalgraphs.graphs.biological import node_generation, edge_generation

# the prefix name corresponds to the meta file in meta/{PREFIX}.meta
prefix = 'ac3'

# read the input segmentation data
segmentation = dataIO.ReadSegmentationData(prefix)

# subset is either training, validation, or testing
subset = 'testing'

# remove the singleton slices
node_generation.RemoveSingletons(prefix, segmentation)
exit()
# generate locations for segments that are too small
node_generation.GenerateNodes(prefix, segmentation, subset)



















# creates a mapping from the segmentation labels to ground truth
seg2gold_mapping = seg2gold.Mapping(segmentation, gold)

# read the manually labeled ground truth data
gold = dataIO.ReadGoldData(prefix)