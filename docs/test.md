<script>
// When the user clicks on <div>, open the popup
function showNotification() {
  if(window.Notification && Notification.permission !== "denied") {
	Notification.requestPermission(function(status) {  // status is "granted", if accepted by user
		var n = new Notification('yo found the easter egg', { 
			body: 'EGG 1/1',
			icon: '/path/to/icon.png' // optional
		}); 
	});
 };
 if(window.Notification && Notification.permission == "denied") {
	alert('denyed   ENTRANCE DENYED');
 };
}
</script>
<p><button onclick="showNotification()">Show a Notification</button></p>
