<!-- Design the look of the admin window Autism app with html. -->
<template>
    <div>
        <!-- Main image section -->
        <h2>Current Image</h2>

        <p>Here you can see your selected image.</p>
        <br />
        <!--Tag input file allows users to choose files from their computers. Restrict types of uploaded files to handle security issues.-->
        <input type="file" accept="image/jpg, image/png, image/jpeg" ref="fileInput" style="display: none" />

        <div v-if="uploadedImages.length > 0">
            <img v-for="image in uploadedImages" :src="image" :key="image" />
        </div>

        <img alt="Image" src="../assets\becduc1.jpg" style="width:800px;height:500px;" /> <!--name of file or the src path should be dynamish to display different images-->
        <!--TODO:display uploaded images from paths in uploadedImages on the website-->
        <!-- document.getElementById('imageContainer').innerHTML = `<img src="${uploadedImages[-1]}" />--> <!--TODO: Only the last uploade image is displayed here-->

        <br />

        <!-- Button section -->
        <!-- When each button is selected, a javascript/python function is called to handle events. -->
        <!-- @click=functionToCall>Displayed Name-->
        <button style="background-color: gray" class="button" type="button" @click="help()">Help</button>
        <button style="background-color: forestgreen" class="button" type="button" @click="openFilePicker()">Upload Image</button>
        <button style="background-color: yellow" class="button" type="button" @click="useWebcam()">Use Webcam</button>
        <button style="background-color: orange" class="button" type="button" @click="deleteImage()">Delete Image</button>
        <button style="background-color: hotpink" class="button" type="button" @click="clearAllImages()">Clear All Images</button>
        <button style="background-color: lightblue" class="button" type="button" @click="detectEmotion()">Emotion Detection</button>

        <br />

        <!-- Other images section -->
        <!-- TODO: Other uploaded images in the uploadedImages are displayed here -->
        <p>Other images are placed here.</p>
        <br />

        <img alt="Image" src="../assets\1.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="../assets\baby1.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="../assets\3.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="../assets\6.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="../assets\5.jpg" style="width:300px;height:300px;" />

        <p></p>
        <br />

    </div>
</template>


<!-- Implement user interaction logic on admin window with javascript. -->
<script>
    export default {
        data() {
            return {
                uploadedImages: [], // Uploaded images are stored in uploadImages array
            };
        },

        methods: {
            help() {
                alert("Help!"); // This method should give users the information how to use these function of the app.
            },
        
            openFilePicker() {
                // Open the file picker to choose images
                this.$refs.fileInput.click();
            },
            async uploadImage() {
                // Get the file input element
                const input = this.$refs.fileInput;

                // Check if a file was selected to handle null pointer exception
                if (input.files.length > 0) {
                    // Get the first selected file
                    const file = input.files[0];

                    // Create a new form data object
                    const formData = new FormData();

                    // Add the file to the form data
                    formData.append('image', file);

                    // Set up the request to interact with server
                    const xhr = new XMLHttpRequest();
                    xhr.open('POST', '/upload-image');

                    // Set up a handler for when the request finishes
                    xhr.onload = () => {
                        if (xhr.status === 200) { // when status code = 200 the upload is successful
                            console.log('Image uploaded successfully');
                            const response = JSON.parse(xhr.responseText);
                            this.uploadedImages.push(response.imageUrl); // save the successful uploaded image in uploadedImages
                        } else {
                            // An error occurred
                            console.log('An error occurred while uploading the image');
                        }
                    };

                    // Send the data
                    xhr.send(formData);
                }
            },
        },
        mounted() {
            this.$refs.fileInput.addEventListener('change', this.uploadImage);
        },

            useWebcam() {
                alert("Webcam is ready!");
            },
            deleteImage() {
                alert("Your image is deleted."); //todo: are you sure to delete the image?
            },
            clearAllImages() {
                alert("All images are cleared."); //todo: are you sure to clear all the images?
            },
            detectEmotion() {
                alert("Waiting for processing of images...");
            }


        
    }


</script>


<!-- Design code style with CSS to make the admin windwo more beautiful.-->
<style scoped>

    .button {
       font-size: 20px;
    }  
    h1 {
        color: forestgreen;
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>

