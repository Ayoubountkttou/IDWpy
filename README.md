# IDWpy
This is a simple code to use IDW interpolation.
The inverse distance weighting (IDW) approach is also known as inverse distance-based weighted interpolation. It is the estimation of the value z at location x by a weighted mean of nearby observations.
 ![image](https://github.com/user-attachments/assets/effecd2a-15e8-4050-9569-606df34f8ff8)
 where
 ![image](https://github.com/user-attachments/assets/a6955c42-4ee4-4238-93cc-8255ba8c1185)

 and where β≥0 and |⋅| corresponds to the euclidean distance. The inverse distance power β  determines the degree to which nearer points are preferred over more distant points. Typically β=1 or β=2, corresponding to an inverse or inverse squared relationship. The number of surrounding points n that are included in the interpolation decides whether a global or local weighting is applied. Both parameters β and n may be fine-tuned by cross-validation, a technique we discuss in more detail in the subsequent sections. If the point x coincides with an observation location (x=xi), then the observed value x is returned to avoid infinite weights.


For references and more detailed:
https://en.wikipedia.org/wiki/Inverse_distance_weighting#:~:text=Inverse%20distance%20weighting%20(IDW)%20is,available%20at%20the%20known%20points.
https://pro.arcgis.com/en/pro-app/latest/help/analysis/geostatistical-analyst/how-inverse-distance-weighted-interpolation-works.htm
https://gisgeography.com/inverse-distance-weighting-idw-interpolation/
