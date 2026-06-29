import api from "./api";

export const getBills = async () => {
    const res = await api.get("/billing/");
    return res.data;
};