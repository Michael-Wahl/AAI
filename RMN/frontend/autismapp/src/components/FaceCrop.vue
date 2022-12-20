<template>
    <div>
      <canvas ref="canvas"></canvas>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ImageCrop',
    props: {
      imageUrl: {
        type: String,
        required: true
      },
      staticImageUrl: {
        type: String,
        required: true
      },
      coordinates: {
        type: Array,
        required: true
      }
    },
    watch: {
      imageUrl: 'cropImage',
      staticImageUrl: 'cropImage',
      coordinates: 'cropImage'
    },
    methods: {
      async cropImage() {
        const image = new Image()
        image.src = this.imageUrl
        await image.decode()
  
        const staticImage = new Image()
        staticImage.src = this.staticImageUrl
        await staticImage.decode()
  
        const canvas = this.$refs.canvas
        const ctx = canvas.getContext('2d')
  
        // Set the canvas dimensions to the same as the static image
        canvas.width = staticImage.width
        canvas.height = staticImage.height
  
        // Draw the static image onto the canvas
        ctx.drawImage(staticImage, 0, 0)
  
        // Draw the cropped image onto the canvas
        ctx.drawImage(
          image,
          this.coordinates[0], // x coordinate of the top-left corner of the source image
          this.coordinates[1], // y coordinate of the top-left corner of the source image
          this.coordinates[2], // width of the source image
          this.coordinates[3], // height of the source image
          350, // x coordinate of the top-left corner of the destination canvas
          50, // y coordinate of the top-left corner of the destination canvas
          this.coordinates[2], // width of the destination canvas
          this.coordinates[3] // height of the destination canvas
        )
      }
    }
  }
  </script>
  