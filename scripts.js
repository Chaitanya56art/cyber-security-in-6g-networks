function encryptData() {
    const data = document.getElementById('data-to-encrypt').value;
    if (data) {
        // Simulate encryption (base64 encoding for demo purposes)
        const encryptedData = btoa(data);
        document.getElementById('encrypted-data').textContent = `Encrypted data: ${encryptedData}`;
    } else {
        alert('Please enter data to encrypt.');
    }
}

function validateEdgeData() {
    const edgeData = document.getElementById('edge-data').value;
    if (edgeData) {
        // Simulate edge data validation
        document.getElementById('edge-validation').textContent = `Data is safe for processing: ${edgeData}`;
    } else {
        alert('Please enter data for edge processing.');
    }
}

function checkAccess() {
    const role = document.getElementById('role').value;
    const networkSlice = document.getElementById('network-slice').value;

    if (role && networkSlice) {
        // Simulate access control check based on role and network slice
        if (role === 'admin' || (role === 'user' && networkSlice !== 'massive_IoT')) {
            document.getElementById('access-status').textContent = 'Access granted.';
        } else {
            document.getElementById('access-status').textContent = 'Access denied. Insufficient permissions.';
        }
    } else {
        alert('Please enter both role and network slice.');
    }
}
