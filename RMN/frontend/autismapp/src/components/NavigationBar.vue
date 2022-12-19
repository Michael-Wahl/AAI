<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">My App</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="home">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavigationBar',
  }
  </script>
  
<style>
.navbar {
  background-color: #222; /* Dark background color */
}

.navbar .navbar-brand {
  color: #fff; /* White text for the brand */
  font-size: 1.5em; /* Large font size for the brand */
  font-weight: bold; /* Bold font weight for the brand */
}

.navbar .nav-item .nav-link {
  color: #fff; /* White text for the links */
  font-size: 1.2em; /* Medium font size for the links */
  font-weight: bold; /* Bold font weight for the links */
  padding: 0.5em 1em; /* Padding for the links */
  border-radius: 0.5em; /* Rounded corners for the links */
  transition: all 0.2s; /* Smooth transition on hover */
}

.navbar .nav-item .nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1); /* Light hover background color */
}
</style>
  