// Function to format time in MM:SS format
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
}

// Add custom event listeners when document is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Add custom styling to audio player if it exists
    const audioPlayer = document.getElementById('audio-player');
    if (audioPlayer) {
        // Update time display
        audioPlayer.addEventListener('timeupdate', function () {
            const currentTime = formatTime(audioPlayer.currentTime);
            const duration = formatTime(audioPlayer.duration || 0);

            // If we have a time display element, update it
            const timeDisplay = document.getElementById('time-display');
            if (timeDisplay) {
                timeDisplay.textContent = `${currentTime} / ${duration}`;
            }
        });

        // Add play/pause functionality
        audioPlayer.addEventListener('play', function () {
            const playButton = document.getElementById('play-button');
            if (playButton) {
                playButton.innerHTML = '<i class="bi bi-pause-fill"></i>';
            }
        });

        audioPlayer.addEventListener('pause', function () {
            const playButton = document.getElementById('play-button');
            if (playButton) {
                playButton.innerHTML = '<i class="bi bi-play-fill"></i>';
            }
        });
    }

    // Form validation
    const lectureForm = document.getElementById('lecture-form');
    if (lectureForm) {
        const topicInput = document.getElementById('topic');

        topicInput.addEventListener('input', function () {
            if (topicInput.value.trim().length > 0) {
                topicInput.classList.remove('is-invalid');
                topicInput.classList.add('is-valid');
            } else {
                topicInput.classList.remove('is-valid');
                topicInput.classList.add('is-invalid');
            }
        });
    }
});