function toggleSchools(element) {
    const townshipId = element.id.split('_')[0];
    const schoolsDiv = document.getElementById(`${townshipId}_schools`);
    const toggleDiv = document.getElementById(`${townshipId}_toggle`);
  
    if (schoolsDiv.style.display === 'none') {
      schoolsDiv.style.display = 'block';
      toggleDiv.innerHTML = `<em>${townshipId}</em>   -`;
    } else {
      schoolsDiv.style.display = 'none';
      toggleDiv.innerHTML = `<em>${townshipId}</em>   +`;
    }
  }
  