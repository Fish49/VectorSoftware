# VectorSoftware
Re-envisioning the way vector manipulation software can work.

## Definitions:
- Object: A singular component. can be a polygon, elipse, curve, point, text, empty, guide, etc
- Group: A conviniant grouping together of related objects
- Drawing: An object made up of one or more curves
- Curve: A collection of connected paths that can either add geometry or cut holes in it
- Path: A section of a curve, with two on-path nodes and zero or more off-path handles between the endpoints
- Node: An on-path point of a curve or other object
- Handle: an off-path point of a curve which defines the shape of the curve