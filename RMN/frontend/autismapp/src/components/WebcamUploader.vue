<template>
  <div>
    <h2>Record Your Emotions</h2>
    <h3>Act out the following emotion: {{ prompts[currentPromptIndex] }}</h3>
    <h3> {{ result }}</h3>
    <br>
    <button @click="toggleSendingImages">{{ isSending ? 'STOP' : 'START' }}</button>
    <button @click="toggleNextEmotion">{{ 'NEXT' }}</button>
    <br>
    <video ref="video" width="640" height="480"></video>
    <canvas ref="canvas" width="640" height="480" class="hidden"></canvas>    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      interval: null,
      video: null,
      canvas: null,
      context: null,
      message: "",
      prompts: ['happy', 'sad', 'neutral', 'angry', 'disgust', 'fear'],
      rec_prompts: [],
      currentPromptIndex: 0,
      result: "Emotion not recognized.",
      isSending: false
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
  },
  methods: {
    //Start/Stop Toggle Button
    toggleSendingImages() {
      if (this.isSending) {
        this.stopSendingImages();
      } else {
        this.startSendingImages();
      }
      this.isSending = !this.isSending;
    },
    //Next Emotion Toggle Button
    toggleNextEmotion() {
      if (this.isSending) {
        if (this.currentPromptIndex++ >= this.prompts.length - 1) {
          this.result == 'You can not skip more emotions.'
        } else {
          this.currentPromptIndex++;
        }
      } else {
        this.result == 'Hit the start button first.'
      }
    },
    isEqual(arr1, arr2) {
      if (arr1.length !== arr2.length) return false;
      for (let i = 0; i < arr2.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
      }
      return true;
    },
    startSendingImages() {
      // Start taking pictures every 1 second
      this.interval = setInterval(() => {
        this.context.drawImage(this.video, 0, 0, 640, 480);

        // Convert the canvas to a data URL and send to server using axios
        const imageData = this.canvas.toDataURL('image/png');
        axios.post('http://127.0.0.1:5000/image-upload', { image: imageData, target: this.prompts[this.currentPromptIndex] },
          { headers: { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' } })
          .then(response => {
            this.message = response.data
            console.log(this.message);
            if (this.message == 'Target matched') {
              this.rec_prompts.push(this.prompts[this.currentPromptIndex])
              this.result = 'Emotion recognized!'
              this.addOverlay()
              if (this.isEqual(this.rec_prompts, this.prompts)) {
                this.result = 'All emotions recorded. You are ready to play!'
                this.stopSendingImages();
              }
              else {
                this.currentPromptIndex++;
                this.result == 'Emotion not recognized.'
              }
            }
          })
          .catch(error => {
            console.error('Error sending image to server: ', error);
          });
      }, 300);
    },
    stopSendingImages() {
      clearInterval(this.interval);
    },
    addOverlay() {
      // Get the video element
      const videoEl = this.$refs.video;

      // Create the overlay element
      const overlayEl = document.createElement('div');
      overlayEl.style.backgroundColor = 'green';
      overlayEl.style.position = 'absolute';
      overlayEl.style.top = '0';
      overlayEl.style.left = '0';
      overlayEl.style.width = '100%';
      overlayEl.style.height = '100%';

      // Create the checkmark icon element
      const iconEl = document.createElement('img');
      iconEl.src = 'https://i.imgflip.com/6hrs2v.png';
      iconEl.style.position = 'absolute';
      iconEl.style.top = '50%';
      iconEl.style.left = '50%';
      iconEl.style.transform = 'translate(-50%, -50%)';
      iconEl.style.width = '100px';
      iconEl.style.height = '100px';

      // Add the checkmark icon to the overlay
      overlayEl.appendChild(iconEl);

      // Add the overlay to the video
      videoEl.parentNode.insertBefore(overlayEl, videoEl.nextSibling);

      // Animate the overlay
      overlayEl.classList.add('fade-in');

      // Fade out the overlay after 2 seconds
      setTimeout(() => {
        overlayEl.classList.add('fade-out');
      }, 2000);

      // Remove the overlay from the DOM when the fade-out animation completes
      overlayEl.addEventListener('animationend', () => {
        overlayEl.parentNode.removeChild(overlayEl);
      });
    }
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
};
</script>

<style>
.hidden {
  display: none;
}

.fade-in {
  animation: fadeIn 0.5s forwards;
}

.fade-out {
  animation: fadeOut 0.5s forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.5;
  }
}

@keyframes fadeOut {
  from {
    opacity: 0.5;
  }
  to {
    opacity: 0;
  }
}
</style>
