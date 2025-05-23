document.addEventListener('DOMContentLoaded', () => {
    fetch('data.json')
        .then(response => response.json())
        .then(customers => {
            const container = document.getElementById('customers-container');
            customers.forEach(customer => {
                const customerDiv = document.createElement('div');
                customerDiv.className = 'customer';
                customerDiv.innerHTML = `
                    <h3>${customer.first_name} ${customer.last_name}</h3>
                    <p>Email: ${customer.email}</p>
                    <hr>
                `;
                container.appendChild(customerDiv);
            });
        })
        .catch(error => console.error('Error loading data:', error));
});