# artsy-download
Download hi-res images from https://www.artsy.net/

## Usage

Install the requirements, then use it like so:

```
python download.py --url https://d32dm0rphc51dk.cloudfront.net/EUo38s6VgQYlkOtEwrBodQ/dztiles/12/5_6.jpg
```

Open the developer console and filter on the image content type. You then need to zoom into the image that you want to download as far as you can and scroll to the bottom right of the image. From the console find the url that has the highest `x_y.jpg` file name. Copy that url and use it as shown above.
