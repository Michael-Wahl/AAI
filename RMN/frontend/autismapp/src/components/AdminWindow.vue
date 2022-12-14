<!-- Design the look of the admin window Autism app with html. -->
<template>
    <div>
        <!-- Main image section -->
        <h2>Current Image</h2>

        <p>Here you can see your selected image.</p>
        <br />
        <!-- <img alt="Image" src="assets/becduc1.jpg" style="width:300px;height:300px;" />-->
        <img alt="Image" src="https://image-us.eva.vn/upload/3-2021/images/2021-09-16/image10-1631783836-199-width650height460.jpg" style="width:800px;height:500px;" />

        <br />

        <!-- Button section -->
        <button>Upload Image</button>
        <button>Use Webcam</button>
        <button>Delete Image</button>
        <button>Clear All Images</button>
        <button>Emotion Detection</button>

        <br />

        <!-- Other images section -->

        <p>Other images are placed here.</p>
        <br />
        <!-- <img alt="Image" src="assets/baby1.jpg" style="width:300px;height:300px;" />-->
        <img alt="Image" src="https://static.politico.com/fa/89/35a03d424d56aabc4fac494aef6b/220128-jim-justice-ap-773.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=640:*" style="width:300px;height:300px;" />
        <img alt="Image" src="https://static.vecteezy.com/system/resources/thumbnails/001/622/736/original/cute-puppy-baby-dog-playing-in-the-green-park-free-video.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="http://akc.org/wp-content/uploads/2018/03/shih-tzu-with-baby-closeup-body.jpg" style="width:300px;height:300px;" />
        <img alt="Image" src="https://i.pinimg.com/originals/e7/1c/f3/e71cf3ea99b31fcdbc3b62ccceb35ae0.jpg" style="width:300px;height:300px;" />
        <!-- variables can be accessed between the {{}} -->
        <p></p>
        <br />

    </div>
</template>


<!-- Implement user interaction logic on admin window with javascript. -->
<script>


    export default {
        data() {
            

        },
       
        methods: {

        }

    };

</script>


<!-- Design code style with CSS to make the admin windwo more beautiful.-->
<style scoped>
    h3 {
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
