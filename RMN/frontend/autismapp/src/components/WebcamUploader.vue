<template>
  <div>
    <video ref="video" width="640" height="480"></video>
    <canvas ref="canvas" width="640" height="480"></canvas>
  </div>
</template>

<script>
export default {
  data() {
    return {
      interval: null,
      video: null,
      canvas: null,
      context: null,
    };
  },
  mounted() {
    this.video = this.$refs.video;
    this.canvas = this.$refs.canvas;
    this.context = this.canvas.getContext("2d");

    // Get access to the webcam
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: false })
      .then(stream => {
        this.video.srcObject = stream;
        this.video.play();
      })
      .catch(err => {
        console.error("Error: ", err);
      });

    // Start taking pictures every 1 second
    this.interval = setInterval(() => {
      this.context.drawImage(this.video, 0, 0, 640, 480);
    }, 1000);
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
};
</script>
