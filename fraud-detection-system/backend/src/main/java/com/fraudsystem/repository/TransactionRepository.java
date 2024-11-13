package com.fraudsystem.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.fraudsystem.model.Transaction;

public interface TransactionRepository extends JpaRepository<Transaction, Integer> {
}
