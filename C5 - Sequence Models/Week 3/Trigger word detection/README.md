raw_data folders have  been zipped for ease of uploading. Unzip them

# How to caculate the count of parameters

## 1DConV

- Input shape: $(None, T_x, n_y) ==> (None, 5511, 101)$
- $T_x = 5511$
- $n_f = 101$
- Filters: $f = 196$
- Kernal Size: $k = 15$
- Stride: $s = 4$
- No padding

- $T_y = (T_x-k)/s + 1 = 1375$
- so the output shape is : $(None, T_y, f) ==> (None, 1375, 196)$
- Parameters Counts : $n_f * f * k + f = (101*196*15) + 196 = 297136$

## GRU
- Input Unit Size: $m = 196$
- Output Unit Size: $n = 128$
- Parameters Counts : $3*(m+n+2)*n ==> 3*(196+128+2)*128 = 125184$
- why +2, two bias?? yes, including additional bias units

## BatchNorm
- Two learnable parameters called beta and gamma
- Two non-learnable parameters (Mean Moving Average and Variance Moving Average)
- Unit Size : $n$
- Parameters Counts: $2*n + 2*n = 4n$

> [!NOTE]
> Useful information that users should know, even when skimming content.