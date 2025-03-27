import '../App.css';
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Member = () => {
    const navigate = useNavigate();
    const [users, setUsers] = useState([]);
    const [editingUser, setEditingUser] = useState(null);

    useEffect(() => {
        fetch("http://localhost:5000/users")
            .then(response => response.json())
            .then(data => setUsers(data))
            .catch(error => console.error("Error fetching users:", error));
    }, []);

    const handleEdit = (user) => {
        setEditingUser(user);
    };

    const handleSave = async () => {
        try {
            await fetch(`http://localhost:5000/update-user`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(editingUser)
            });
            setUsers(users.map(user => user.id === editingUser.id ? editingUser : user));
            setEditingUser(null);
        } catch (error) {
            console.error("Error updating user:", error);
        }
    };

    const handleDelete = async (userId) => {
        const confirmDelete = window.confirm("Are you sure you want to delete this user?");
        if (confirmDelete) {
            try {
                await fetch(`http://localhost:5000/delete-user/${userId}`, {
                    method: "DELETE",
                    headers: { "Content-Type": "application/json" },
                });
                setUsers(users.filter(user => user.id !== userId)); // Remove deleted user from the UI
            } catch (error) {
                console.error("Error deleting user:", error);
            }
        }
    };

    return (
        <div className="Container-home">
            <p className='Text-Welcome'>Members</p>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Password</th>
                        <th>Role</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map(user => (
                        <tr key={user.id}>
                            <td>
                                {editingUser?.id === user.id ? (
                                    <input type="text" value={editingUser.username} onChange={(e) => setEditingUser({...editingUser, username: e.target.value})} />
                                ) : user.username}
                            </td>
                            <td>
                                {editingUser?.id === user.id ? (
                                    <input type="text" value={editingUser.password} onChange={(e) => setEditingUser({...editingUser, password: e.target.value})} />
                                ) : user.password}
                            </td>
                            <td>
                                {editingUser?.id === user.id ? (
                                    <select value={editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: e.target.value})}>
                                        <option value="Dev">Dev</option>
                                        <option value="Admin">Admin</option>
                                        <option value="User">User</option>
                                    </select>
                                ) : user.role}
                            </td>
                            <td>
                                {editingUser?.id === user.id ? (
                                    <button onClick={handleSave}>Save</button>
                                ) : (
                                    <>
                                        <button onClick={() => handleEdit(user)}>Edit</button>
                                        <button onClick={() => handleDelete(user.id)}>Delete</button>
                                    </>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Member;
