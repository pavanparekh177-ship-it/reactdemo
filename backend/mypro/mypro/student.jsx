import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getStudents, deleteStudent } from "../api/studentApi";

const Students = () => {
    const [students, setStudents] = useState([]);

useEffect(() => {
    getStudents().then(res => setStudents(res.data));
}, []);

return (
    <div>
    <h1>Students List</h1>
    <Link to="/add">+ Add Student</Link>
    <table border="1">
        <thead>
        <tr>
            <th>Name</th><th>Email</th><th>Phone</th><th>Actions</th>
        </tr>
        </thead>
        <tbody>
        {students.map(s => (
        <tr key={s.id}>
            <td>{s.name}</td>
            <td>{s.email}</td>
            <td>{s.phone}</td>
            <td>
            <Link to={`/edit/${s.id}`}>Edit</Link>
            <button onClick={() => deleteStudent(s.id)}>Delete</button>
            </td>
        </tr>
        ))}
        </tbody>
    </table>
    </div>
);
};

export default Students;
