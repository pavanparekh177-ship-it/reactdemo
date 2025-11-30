import axios from "axios";

const API = "http://127.0.0.1:8000/api/students";

export const getStudents = () => axios.get(API);
export const addStudent = (data) => axios.post(`${API}/add/`, data);
export const updateStudent = (id, data) => axios.put(`${API}/update/${id}/`, data);
export const deleteStudent = (id) => axios.delete(`${API}/delete/${id}/`);
