import React, { useState, useEffect } from 'react';

const TransactionList = () => {
    const [transactions, setTransactions] = useState([]);
    
    useEffect(() => {
        fetch('/api/transactions')
            .then(response => response.json())
            .then(data => setTransactions(data));
    }, []);

    return (
        <div>
            <h2>Transaction List</h2>
            <table>
                <thead>
                    <tr>
                        <th>Transaction ID</th>
                        <th>Amount</th>
                        <th>Location</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map(transaction => (
                        <tr key={transaction.transactionId}>
                            <td>{transaction.transactionId}</td>
                            <td>{transaction.transactionAmount}</td>
                            <td>{transaction.location}</td>
                            <td>{transaction.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default TransactionList;
